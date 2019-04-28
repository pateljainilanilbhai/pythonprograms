import threading
from bs4 import BeautifulSoup
import requests
def heron(a):

    while True:
        try:
            url = 'http://www.jio.com'
            r = requests.get(url)
        except:
            print("This is an error message!")
    return new


threading._start_new_thread(heron,(99,))
threading._start_new_thread(heron,(999,))
threading._start_new_thread(heron,(1733,))
threading._start_new_thread(heron,(992,))
threading._start_new_thread(heron,(9992,))
threading._start_new_thread(heron,(17332,))
threading._start_new_thread(heron,(994,))
threading._start_new_thread(heron,(999,))
threading._start_new_thread(heron,(17353,))
threading._start_new_thread(heron,(995,))
threading._start_new_thread(heron,(9999,))
threading._start_new_thread(heron,(1733658,))
threading._start_new_thread(heron,(9954,))
threading._start_new_thread(heron,(99954,))
threading._start_new_thread(heron,(17336845,))
threading._start_new_thread(heron,(9954,))
threading._start_new_thread(heron,(99954,))
threading._start_new_thread(heron,(1733864,))


for i in range(0,10000):
    url = 'http://www.jio.com'
    r = requests.get(url)
    r_html = r.text
    soup = BeautifulSoup(r_html, "lxml")
    print(soup)



# for titles in soup.find_all(class_="story"):
# 	title = titles.a
# 	print(title.string)