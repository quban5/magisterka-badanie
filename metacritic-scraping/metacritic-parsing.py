import time
import sys
import requests
from bs4 import BeautifulSoup

with open('metacritic-scraping/strony/Page1.html') as Page1:
    soup = BeautifulSoup(Page1, 'html.parser')

allSpans = soup.select('.c-finderProductCard_titleHeading span')


SpansIndex = 2

while SpansIndex <= 48:
    for Spans in allSpans[:SpansIndex]:
        Game = Spans.get_text(strip=True)

    print(Game)
    SpansIndex = SpansIndex + 2