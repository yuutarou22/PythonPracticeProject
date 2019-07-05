import requests
from bs4 import BeautifulSoup

html = requests.get('https://news.yahoo.co.jp/')

yahoo = BeautifulSoup(html.content, "html.parser")

for title in yahoo.select("ul.toptopics_list"):
	print (title.getText())

print('------------------')

print(html.encoding)


