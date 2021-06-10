
import pymysql
from pymysql import converters
BITCOIN_API = "http://api.coindesk.com/v1/bpi/historical/close.json?start={start_date}&end={end_date}&currency={currency}"

conv = converters.conversions.copy()
conv[246] = float    # convert decimals to floats
conv[10] = str
conv[12] = str

DATABASE = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'dark_web',
    'conv': conv,
}


connection = pymysql.connect(**DATABASE)
connection.commit()
cursor = connection.cursor()
