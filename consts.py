from enum import Enum
class VARS(Enum):
    url = 'http://www.stockpup.com'
    data_dir = './data'
    raw_dir = '/raw/'
    cleaned_dir = '/clean/'  # DATA THAT IS CORRECT
    uncleaned_dir = '/unclean/'
    cleanFormat = open('./data/sample.csv').read().splitlines()[0]

