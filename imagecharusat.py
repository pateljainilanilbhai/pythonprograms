import requests
from bs4 import BeautifulSoup
import urllib.request
from PIL import Image
from io import BytesIO



def get_images(link,name):
    print(link)
    response = requests.get(link)
    img = Image.open(BytesIO(response.content))
    print(img)
    img.save(name+".jpg")


def spider(url):


    source_code=requests.get(url)
    plaintext=source_code.text;
    soup=BeautifulSoup(plaintext,'html.parser')
    print(soup.prettify())
    for link in soup.find_all('img'):
        if link.get('height')!=60:
            img_link=str(link.get('src'))
            name=img_link[34:len(img_link)-4]
            try:
                get_images("https://www.charusat.ac.in"+img_link,name)
            except:
                pass
            print("https://www.charusat.ac.in"+img_link)

spider("https://www.charusat.ac.in/CSPIT/computer-engineering/faculty-members/")