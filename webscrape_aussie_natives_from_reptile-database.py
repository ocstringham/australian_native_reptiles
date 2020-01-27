# load in libraries
from bs4 import BeautifulSoup
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
import pandas as pd


# start requests session: https://stackoverflow.com/questions/23013220/max-retries-exceeded-with-url-in-requests?rq=1
session = requests.Session()
retry = Retry(connect = 5, status = 5, read =5, backoff_factor = 2) # https://urllib3.readthedocs.io/en/latest/reference/urllib3.util.html#module-urllib3.util.retry
adapter = HTTPAdapter(max_retries=retry)
session.mount('http://', adapter)
session.mount('https://', adapter)
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
session.headers.update({'User-Agent': user_agent})
    

# url search for all species with distribs in Australia
url = 'http://reptile-database.reptarium.cz/advanced_search?location=Australia&submit=Search'

## visit  page
page = session.get(url, allow_redirects=True)
soup = BeautifulSoup(page.text, 'html.parser')

## get sp names
list_elem = soup.find('h2', text = 'Search results')
sp_ul = list_elem.find_next('ul')

## save sp names to list
sp = [ elem.find('em').text.strip() for elem in sp_ul.find_all('li') ]


# same search except remove species that say 'introduced' in distrib
url2 = 'http://reptile-database.reptarium.cz/advanced_search?location=Australia+-introduced&submit=Search'

## visit  page
page = session.get(url2, allow_redirects=True)
soup = BeautifulSoup(page.text, 'html.parser')

## get sp names
list_elem = soup.find('h2', text = 'Search results')
sp_ul = list_elem.find_next('ul')

## save to list
sp2 = [ elem.find('em').text.strip() for elem in sp_ul.find_all('li') ]


# get differences between lists
diff = list(set(sp) - set(sp2))


# manually check differences to see if species is non native to Aus OR native to Aus but non native elsewhere

## define non natives to austrlia
nn = ['Hemidactylus frenatus', 'Trachemys scripta']


# remove non native to australia species
natives = [x for x in sp if x not in nn]


# to csv
natives.to_csv('aus_native_reptiles.csv')