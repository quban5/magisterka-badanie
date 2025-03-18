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
EstimatedTime = DesiredPages * 10 / 60 #Multiplying DesiredPages by 10 seconds and dividing the outcome by 60 to get number of minutes


print("The script will be running for about: ", EstimatedTime, " minutes.")
ContinueStop = input("Do you want to continue? (y/n): ")

if ContinueStop == "y":
    for TargetPage in range(1, DesiredPages + 1):
        if TargetPage <= DesiredPages:
            url = f"https://www.metacritic.com/browse/game/pc/all/all-time/metascore/?releaseYearMin=1958&releaseYearMax=2015&platform=pc&page={TargetPage}"
            r = requests.get(url, headers=headers)
            save_html(r.content, f"/home/jakub/Studia/magisterka-badanie/metacritic-scraping/pages/Page{TargetPage}.html")
            print("Pages scraped: ", TargetPage, " / ", DesiredPages)
            print("First 10 characters of scraped page: ", r.content[:10])
            print("Waiting for 10 seconds...")
            TargetPage + 1
            time.sleep(10)

    print("Done. ", TargetPage, " / ", DesiredPages, " pages scraped.")            
    input("Press enter to close the script")
else:
    exit()

exit()
