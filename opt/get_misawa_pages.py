#coding: utf-8

import requests
from bs4 import BeautifulSoup

url = "http://blog.livedoor.jp/jigokuno_misawa/eid_69773305.html"
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'html.parser')

# div.article-body-inner->div->img src 画像
body_inner = soup.find('div', {'class': 'article-body-inner'})
img = body_inner.find('img').get('src')
print(img)
# div.article-body-inner->div->img alt 画像内文字
alt = body_inner.find('img').get('alt')
print(alt)
# div.article-category->a->text キャラ名
category = soup.find('div', {'class': 'article-category'})
characeter = category.find('a').get_text()
print(characeter)

# with open("test.txt", "w") as f:
#     f.write(html)

next_page = soup.find('div', {'class': 'nextPage'})
link = next_page.find('a').get('href')
print(link)

# with open("test.txt", "w") as f:
    # f.write(html)