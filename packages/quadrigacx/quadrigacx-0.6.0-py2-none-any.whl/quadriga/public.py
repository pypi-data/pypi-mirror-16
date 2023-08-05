import requests
from quadriga import check_list_value, check_value

try:
    from lobgect import log
    lobject_support = True
except ImportError:
    import logging
    lobject_support = False

if lobject_support:
    logger = log.Log(__name__)
else:
    logger = logging.getLogger(__name__)
    logger.log_variables = lambda x: x
    logger.print_post_data = lambda x: x

def _get(url, params):
    return requests.get( url, params=params ).json()

@logger.log_variables
def ticker(unchecked_book_list=None):
    logger.info('Getting current trading information.')
    url = 'https://api.quadrigacx.com/v2/ticker'
    books = check_list_value(unchecked_book_list, known_good_options=['btc_cad', 'btc_usd', 'eth_btc', 'eth_cad'])
    response_data = {}

    for book in books:
        params = { 'book': book }
        response_data[book] = _get( url, params )

    logger.info(books)
    return response_data

@logger.log_variables
def order_book(unchecked_book_list=None, group_transactions=False):
    logger.info('Getting live order book.')
    url = 'https://api.quadrigacx.com/v2/order_book'
    books = check_list_value(unchecked_book_list, known_good_options=['btc_cad', 'btc_usd', 'eth_btc', 'eth_cad'])
    group = check_value(group_transactions, expected_type=bool)
    response_data = {}

    for book in books:
        params = { 'book': book, 'group': 1 if group_transactions else 0 }
        response_data[book] = _get( url, params )

    return response_data

@logger.log_variables
def transactions(unchecked_book_list=None, unchecked_time_frame='hour'):
    url = 'https://api.quadrigacx.com/v2/transactions'
    books = check_list_value(unchecked_book_list, known_good_options=['btc_cad', 'btc_usd', 'eth_btc', 'eth_cad'])
    time_frame = check_value(unchecked_time_frame, default_value='hour', known_good_options=['hour', 'minute'])
    response_data = {}

    logger.info('Getting transactions from the last {}.'.format(time_frame))

    for book in books:
        params = { 'book': book, 'time': time_frame }
        response_data[book] = _get( url, params )

    return response_data
