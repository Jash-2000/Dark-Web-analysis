#!/usr/bin/env python
""" Controls actions on the database """
import pandas
from pprint import pprint
from pymysql import converters
import pymysql

import logic
import settings
from db_patches import db_patches_list


def query(query_string, items=None, safe_mode=True):
    """ Given a query string returns a cursor object """
    valid_query = validate_query(query_string, safe_mode)
    if valid_query:
        connection = pymysql.connect(**settings.DATABASE)
        cursor = connection.cursor()
        cursor.execute(query_string, items)
        if not safe_mode:
            connection.commit()
        return cursor
    else:
        raise Exception(
            'SQL verbs that alter schema are not allowed in safe mode')


def pandas_query(query_string, safe_mode=True, *args, **kwargs):
    """Given a query string returns a pandas Dataframe"""
    valid_query = validate_query(query_string, safe_mode)
    if valid_query:
        con = settings.connection
        return pandas.read_sql(query_string, con=con, *args, **kwargs)
    else:
        raise Exception(
            'SQL verbs that alter schema are not allowed in safe mode')


def validate_query(query_string, safe_mode):
    """On safe mode, reject schema alterations """
    verbs_not_allowed = ['create, alter, grant']
    if safe_mode:
        if any(verb in query_string.lower() for verb in verbs_not_allowed):
            return False

    return True


def validate_patches():
    """ Ensure that the required db patches have been applied
    and applies those requireds
    """
    for patch in db_patches_list():
        print ("##### validating patch %s ####" % (patch.name))
        is_valid = query(patch.validation, safe_mode=False)
        if is_valid:
            print ('Validation OK')
        else:
            print ('Not valid - Applying patch ...')
            query(patch.sql, safe_mode=False)


def get_products_by_subcategory(category_name):
    return pandas_query('''
        SELECT * FROM dark_web.tblProduct
        WHERE subCategory_id in
            (select subCategory_id from tblSubCategory
                where subCategory_name = '{}');
        '''.format(category_name))


def get_product_bitcoin_prices():
    return query('SELECT product_id, product_price, time_stamp from tblProduct;')


def insert_converted_prices(currency, start_date, end_date):
    print ('### Pulling bitcoin price indexes in {} ###'.format(currency))
    rates_dict = logic.get_bitcoin_conversions(currency, start_date, end_date)
    products = get_product_bitcoin_prices()
    print('#### Updating Records ###')
    for product in products.fetchall():
        sql = '''
            UPDATE tblProduct SET {} = {}
            where product_id = {}
            '''.format(
                currency,
                float(rates_dict.get(product[2])) * float(product[1].split(' ')[0]),
                product[0]
                )
        print (sql)
        q = query(sql, safe_mode=False)
    return True  # query(sql, items)


#rates = insert_converted_prices('GBP', '2015-01-01', '2016-01-01')
#q = pandas_query('SELECT * FROM tblProduct limit 10')
