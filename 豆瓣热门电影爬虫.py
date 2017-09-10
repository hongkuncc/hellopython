#coding: utf-8
#python2.7
import urllib2
from bs4 import BeautifulSoup
print "豆瓣正在热映："
url="https://movie.douban.com"
html=urllib2.urlopen(url).read()#用urllib模块把豆瓣网页抓下来
soup=BeautifulSoup(html)
div_hot=soup.find('div',{"id":"screening"})#截取需要的部分（"id"=screening）
for i in div_hot.find_all('li',class_='title'):#class为关键字故不能直接用
    movie_title=i.a.get_text()
    movie_title=movie_title.strip()#去除空格
    print movie_title
print"\n豆瓣最近热门："
#div_new=soup.find('div',{"id":"new-movies"})
#for i in div_new.find_all('li',class_='title'):
#   movie_new=i.a.get_text()
#    print movie_new
