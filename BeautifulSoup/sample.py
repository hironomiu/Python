import bs4
import os
import requests

# 入力からの解析
soup = bs4.BeautifulSoup("<p>Some<b>bad<i>HTML", "lxml")
print(soup.prettify())
print(soup.find(text="bad"))

print('--'*20)

# ローカルファイルからの解析
soup = bs4.BeautifulSoup(
    open(os.path.dirname(__file__) + '/html/sample.html'), 'lxml')
print(soup.prettify())
print(soup.find(text="hoge"))
print(soup.i)

print('--'*20)

soup = bs4.BeautifulSoup(
    open(os.path.dirname(__file__) + '/html/sample2.html'), 'lxml')
print(soup.prettify())
print(soup.find(text="bad"))
print(soup.i)

print('--'*20)

# webからの解析
url = "http://google.com"
req = requests.get(url)

soup = bs4.BeautifulSoup(req.text, 'lxml')
print(soup.h1)
print(soup.div)
print(soup.find(text="Google"))
