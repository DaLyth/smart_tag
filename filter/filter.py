# Takes the url as the first argument.

from lxml import html
from lxml import etree
from bs4 import BeautifulSoup
import requests
import sys
import string
import unicodedata

print 'Fetching ' + sys.argv[1] + '\n'

url = sys.argv[1]

page = requests.get(url)


tree = html.fromstring(page.content)

intro1 = tree.xpath('//*[@id="mw-content-text"]/p[1]')
intro2 = tree.xpath('//*[@id="mw-content-text"]/p[2]')
intro3 = tree.xpath('//*[@id="mw-content-text"]/p[3]')
intro4 = tree.xpath('//*[@id="mw-content-text"]/div[2]')


intro_string1 = etree.tostring(intro1[0])
intro_string2 = etree.tostring(intro2[0])
intro_string3 = etree.tostring(intro3[0])
intro_string4 = etree.tostring(intro4[0])

soup1  = BeautifulSoup(intro_string1, 'html.parser')
soup2  = BeautifulSoup(intro_string2, 'html.parser')
soup3  = BeautifulSoup(intro_string3, 'html.parser')
soup4  = BeautifulSoup(intro_string4, 'html.parser')

print 'Writing to \'filtered_' + url[30:] + '\'\n'

f = open('filtered_' + url[30:], 'w')

toDisk = soup1.get_text() + soup2.get_text() + soup3.get_text() + soup4.get_text()

toDisk = toDisk.encode('ascii','ignore')


f.write(toDisk)
