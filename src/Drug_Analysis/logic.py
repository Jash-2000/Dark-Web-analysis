import settings
import requests

VALID_UNITS = {
    'g': ['g','gram', 'gr', 'grams', 'grs']

    }

NUMBER_STRING = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'ten': 10, 
}



def get_bitcoin_conversions(currency, start_date, end_date):
    """
    Given a currency code, start date and end date,
    returns dict with daily bitcoin conversion
    """
    api_url = settings.BITCOIN_API.format(
        start_date=start_date,
        end_date=end_date,
        currency=currency
        )
    request = requests.get(api_url)
    return request.json().get('bpi')

