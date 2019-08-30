from consts import VARS
import requests
import time
import os
from bs4 import BeautifulSoup
import urllib





def downloadData(data):

    print('Downloading data...')
    for record in data:
        download_url = VARS.url.value + record[1]
        try:
            print("Downloading {}...".format(record[0]))
            urllib.request.urlretrieve(download_url, './data/raw/{}'.format(record[0]))
        except:
            print('Could not download {}'.format(record[0]))
        if 'ZTS' in download_url:
            return

def updateList():
    global done

    response = ''
    nurls = []
    f = ''

    print('Updating data... ')


    try:
        response = requests.get(VARS.url.value+"/data")
    except:
        raise Exception('Could not fetch url!')
    try:
        print('Parsing data...')
        response = BeautifulSoup(response.text, 'html.parser').findAll('a')
        response = list(filter(lambda x: 'CSV' in x, response))
        for param in response:
            nurls.append([param['title'], param['href']])
    except:
        raise Exception('Could not parse data! Do you have BS4 installed?')
    try:
        cdir = os.path.join(VARS.data_dir.value, VARS.raw_dir.value)
        if not os.path.exists(cdir):
            os.mkdir(cdir)
    except:
        raise Exception('Could not make directory!')

    downloadData(nurls)



if __name__ == '__main__':
    updateList()

