import time
import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup



def save_html(html, path):
    with open(path, 'wb') as f:
        f.write(html)



ua = UserAgent()
headers = {'user-agent': ua.random}


print("User agent is:")
print(" ")
print(ua.random)
input("Press enter to continue...")


DesiredPages = int(input("Enter number of pages you want to scrap: "))
TargetPage = 1
url = "https://www.metacritic.com/browse/game/pc/all/all-time/metascore/?releaseYearMin=1958&releaseYearMax=2015&platform=pc&page=", TargetPage


print("First page you are about to scrap is: ", url)
ContinueStop = input("Do you want to continue? (y/n): ")

if ContinueStop == "y":
    for DesiredPages:
        if TargetPage < DesiredPage and TargetPage == DesiredPage:
            r = requests.get(url, headers=headers)
            save_html(r.content, "Page"TargetPage".html")
            print("Scraped page: ", TargetPage)
            print("First 10 characters of scraped page: ", r.content[:10])
            time.sleep(10)
            print("Waiting for 10 seconds...")
        else:
            input("Done. Press enter to close script")
            exit()
else:
    exit()
