import requests
from bs4 import BeautifulSoup as bs

url = "http://www.ttkmj.tv/archives/40.html"

r = requests.get(url)
soup = bs(r.text, 'html.parser')

res = soup.find('tbody').find_all('a')
link = []
for r in res:
    if r.get('href') and (r.get('href').startswith('magnet') or r.get('href').startswith('ed2k')):
        link.append(r.get('href'))
print('\n'.join(link))
