#coding: utf-8

import requests
from bs4 import BeautifulSoup

url = "http://blog.livedoor.jp/jigokuno_misawa/eid_69773305.html"
response = requests.get(url)
html = response.text

# div.article-body-inner->div->img src
# div.article-body-inner->div->img alt
# div.article-category->a->text

soup = BeautifulSoup(html, 'html.parser')
next_page = soup.find('div', {'class': 'nextPage'})
link = next_page.find('a').get('href')
print(link)

# with open("test.txt", "w") as f:
    # f.write(html)