import time
import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup



def save_html(html, path):
    with open(path, 'wb') as f:
        f.write(html)



ua = UserAgent()

print(ua.random)

time.sleep(2)

url = 'https://szaniec.pttk.pl/imprezy.html'

headers = {'user-agent': ua.random}

r = requests.get(url, headers=headers)

save_html(r.content, 'Page1.html')

print(r.content[:10])

print('gotowe')

time.sleep(2)
