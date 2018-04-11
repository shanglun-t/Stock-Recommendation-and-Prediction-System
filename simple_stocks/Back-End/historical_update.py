import os
import sys
import csv
import time
import requests
from datetime import datetime, timedelta
from bs4 import BeautifulSoup 
from math import floor

TICKER = "AAL"  # line for testing - disable when updating entire directory
DATA_ROOT = os.getcwd()
DATA_PATH = DATA_ROOT + "/historical_data/"

SITE_URL = 'https://finance.yahoo.com'

# today's timestemp
now = datetime.now()
tDate = now.strftime('%s')

# start-date's timestemp
delta = now - timedelta(days=3650)
sDate = delta.strftime('%s')

PAGE_URL = SITE_URL + '/quote/' + TICKER + '/history?period1=' + sDate + '&period2=' + tDate + '&interval=1d&filter=history&frequency=1d'

time.sleep(45)  # waiting for loading 3650 rows

DATA_FILE = TICKER + ".csv"
DATA_URL = DATA_PATH + DATA_FILE
   
source = requests.get(PAGE_URL).text
soup = BeautifulSoup(source, 'lxml')
    
csv_file = open(DATA_URL, 'w') 
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume'])

for tr in soup.find_all('tr', class_='BdT Bdc($c-fuji-grey-c) Ta(end) Fz(s) Whs(nw)'):
    
    Date = tr.find_all('td')[0].text
    Open = tr.find_all('td')[1].text
    High = tr.find_all('td')[2].text
    Low = tr.find_all('td')[3].text
    Close = tr.find_all('td')[4].text
    Adj_Close = tr.find_all('td')[5].text
    Volume = tr.find_all('td')[6].text
        
    csv_writer.writerow([Date, Open, High, Low, Close, Adj_Close, Volume])

csv_file.close()        
        
'''
# updating entire "historical_data" directory

for TICKER in listdir(DATA_PATH):
    # https://finance.yahoo.com/quote/AAPL/history?period1=1207724400&period2=1523257200&interval=1d&filter=history&frequency=1d
    PAGE_URL = SITE_URL + '/quote/' + TICKER + '/history?period1=' + sDate + '&period2=' + eDate + '&interval=1d&filter=history&frequency=1d'
    
    time.sleep(45)
    
    DATA_FILE = TICKER + ".csv"
    DATA_URL = DATA_PATH + DATA_FILE
    
    source = requests.get(PAGE_URL).text
    soup = BeautifulSoup(source, 'lxml')
    
    csv_file = open(DATA_URL, 'w') 
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume'])
    
    for tr in soup.find_all('tr', class_='BdT Bdc($c-fuji-grey-c) Ta(end) Fz(s) Whs(nw)'):
        
        Date = tr.find_all('td')[0].get_text()
        Open = tr.find_all('td')[1].get_text()
        High = tr.find_all('td')[2].get_text()
        Low = tr.find_all('td')[3].get_text()
        Close = tr.find_all('td')[4].get_text()
        Adj_Close = tr.find_all('td')[5].get_text()
        Volume = tr.find_all('td')[6].get_text()
        
        csv_writer.writerow([Date, Open, High, Low, Close, Adj_Close, Volume])
        
    
    csv_file.close()
'''
    
    
    
    




