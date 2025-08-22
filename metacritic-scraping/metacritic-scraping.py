import time                                                                     # Zaimportowanie bibliotek potrzebnych do działania.
import requests                                                                 # Fake user agent potrzebny jest, aby strona metacritica "myślała", 
from fake_useragent import UserAgent                                            # że żądania html wysyła człowiek, a nie skrypt.



def save_html(html, path):                                                      # Utworzenie funkcji save_html o dwóch wejściach: html i path.
    with open(path, 'wb') as f:                                                 # Otwiera plik, którego lokalizacja zdeterminowana jest przez path i tworzy obiekt o nazwie f.
        f.write(html)                                                           # Zapisuje zawartość zmiennej html do pliku o nazwie f.

ua = UserAgent()                                                                # Zamiast UserAgent używana będzie krótsza nazwa ua
headers = {'user-agent': ua.random}                                             # Zapisanie do zmiennej headers informacji. User agent jest generowany losowo przez ua.random.





print("User agent is:")                                                         # 
print(ua.random)                                                                # Program podaje jaki user agent został wylosowany.
print(" ")                                                                      #
input("Press enter to continue...")                                             # Program czeka na wciśnięcie Enter, żeby kontynuować dalej.


DesiredPages = int(input("Enter number of pages you want to scrap: "))          # Program pyta się ile stron chcemy zescrapować i zapisuje to do zmiennej DesiredPages.
TargetPage = 1                                                                  # Ustawienie wartości początkowej 1. TargetPage to zmienna, która przetrzymuje numer strony, który zostanie zescrapowany.


EstimatedTime = DesiredPages * 10 / 60                                          # Pomnożenie DesiredPages przez 10 i podzielenie wyniku przez 60, żeby uzyskać ile około minut zajmie cały proces scrapowania.


print("The script will be running for about: ", EstimatedTime, " minutes.")     # Program podaje ile mniej więcej będzie scrapował strony
ContinueStop = input("Do you want to continue? (y/n): ")                        # i pyta się czy kontynuować. Jeśli "y" (yes) kontynuuje, jeśli "n" (no) zamyka program.

if ContinueStop == "y":                                                                                                                                         # Jeśli "y" (yes), to zaczyna działać. Jeśli "n" (no), zamyka program.
    for TargetPage in range(1, DesiredPages + 1):                                                                                                               # Dla każdej podanej przez użytkownika liczby stron,
        if TargetPage <= DesiredPages:                                                                                                                          # dopóki TargetPage jest mniejsze lub równe DesiredPages, dopóty program działa.
            url = f"https://www.metacritic.com/browse/game/pc/all/all-time/metascore/?releaseYearMin=1958&releaseYearMax=2015&platform=pc&page={TargetPage}"    # Ustanawianie zmiennej url na odpowiednią stronę metacritic.com. TargetPage na końcu linku odpowiada za kolejne strony.
            r = requests.get(url, headers=headers)                                                                                                              # Biblioteka requests wysyła żądanie html do powyższego url z headerem o wcześniej wylosowanym user agent. To polecenie nazywa się to teraz r.
            save_html(r.content, f"/home/jakub/Studia/magisterka-badanie/metacritic-scraping/pages/Page{TargetPage}.html")                                      # Funkcja save_html zapisuje stronę metacritica w html trzymaną w wartości r.content w podanej lokalizacji i z nazwą swojej strony, np. Page1.html.
            print("Pages scraped: ", TargetPage, " / ", DesiredPages)                                                                                           # Program informuje ile stron zdążył zescrapować i ile zostało.
            if TargetPage < DesiredPages:                                                                                                                       # Jeśli program nadal nie zescrapował wszystkich potrzebnych stron, będzie czekał 10 sekund, przed wysłaniem następnego żądania, aby nie dostać bana od serwera metacritic.
                print("Waiting for 10 seconds...")                                                                                                              #
                TargetPage + 1                                                                                                                                  # Wartość TargetPage zwiększamy o 1, ponieważ chcemy następnie zescrapować kolejną stronę.
                for Second in range(1,11):                                                                                                                      # Program czeka 10 sekund i wyświetla aktualną ilość czekanych sekund.
                    print(Second, end="\r")                                                                                                                     #
                    time.sleep(1)                                                                                                                               #

    print("Done. ", TargetPage, " / ", DesiredPages, " pages scraped.")                                                                                         # Kiedy pętla się skończy i wszystkie strony zostaną zescrapowane, program komunikuje, że skończył i podaje ile stron zescrapował.
    input("Press enter to close the script")                                                                                                                    # Czeka na naciśnięcie Enter, zanim zamknie się program.
else:
    exit()

exit()