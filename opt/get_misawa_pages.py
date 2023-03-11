#coding: utf-8

import requests
from bs4 import BeautifulSoup

url = "https://www.google.com"
response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, 'html.parser')
title = soup.title.string
print(title)
with open("test.txt", "w") as f:
    f.write(title)
# search_form = soup.find('form', {'class': 'tsf'})
# input_tag = search_form.find('input', {'name': 'q'})
# input_name = input_tag['name']
# print(input_name)