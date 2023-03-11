#coding: utf-8

import requests
from bs4 import BeautifulSoup

url = "https://www.google.com"
response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, 'html.parser')
title = soup.title.string
print(title)