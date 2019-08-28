from animations import animate, done
import requests
import threading
import time
import os
from bs4 import BeautifulSoup
import urllib

# VARIABLES FOR STOCK DATA
url = 'http://www.stockpup.com'
data_dir = './data'
raw_dir = '/raw/'
cleaned_dir = '/clean/' #DATA THAT IS CORRECT
uncleaned_dir = '/unclean/'




def downloadData(data):
    global done

    print('Downloading data...')
    for record in data:
        download_url = url + record[1]
        print(download_url)
        done = False
        t = threading.Thread(target=animate, args=['Downloading ' + record[0]])
        t.start()
        # urllib.request.urlretrieve
        done = True

def updateList():
    global done

    response = ''
    nurls = []
    f = ''

    print('Updating data... ')


    try:
        response = requests.get(url+"/data")
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
        cdir = os.path.join(data_dir, raw_dir)
        if not os.path.exists(cdir):
            os.mkdir(cdir)
    except:
        raise Exception('Could not make directory!')
    print(nurls)
    downloadData(nurls)



if __name__ == '__main__':
    updateList()

