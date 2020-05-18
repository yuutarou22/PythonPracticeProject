import sys

import requests
from bs4 import BeautifulSoup

args = sys.argv

print(args)

if 2!=len(args):
    print('引数がダメです。')
else:
    print('引数はOKです。')

print('------------------')

html = requests.get('https://app.neilpatel.com/jp/ubersuggest/overview?lang=ja&locId=2392&keyword=' + args[1] + '+')

print(html.content)

result_html = BeautifulSoup(html.content, "html.parser")

for title in result_html.select(".css-63oe3q"):
	print (title.getText())

print('------------------')

print(html.encoding)