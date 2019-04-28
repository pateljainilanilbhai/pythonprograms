from bs4 import BeautifulSoup as soup
import requests
import re

my_url = 'https://www.nytimes.com'

# opening connection, grabbing the page.
r = requests.get(my_url)
page_html = r.text

# html parsing
page_soup = soup(page_html, 'html.parser')


# grabs each story header and stores into a list
stories = page_html

print("Total number of stories: " + str(len(stories)) + ". \n")

open_file = open('file_to_save.txt', 'w')

# Regex to eliminate tags and characters. Lstrip and rstrip to remove whitespaces/newlines.
for b in stories:
    content = str(re.sub("<.*?>", "", str(b))).lstrip().rstrip()
    open_file.write('\n' + content)

open_file.close()