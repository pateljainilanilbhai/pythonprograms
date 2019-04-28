#web scrapping with python
import re
from bs4 import BeautifulSoup
import requests

soup=BeautifulSoup(requests.get("http://www.charusat.ac.in").content,features="lxml")

print(soup.prettify())

for link in soup.find_all('a'):
    print(link.get('href'))
