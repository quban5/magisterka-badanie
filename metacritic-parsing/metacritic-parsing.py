from bs4 import BeautifulSoup
import json


def getGameRank(indexOfGameRank):                                                       # Spany w klasie .c-finderProductCard_titleHeading są dwa: numer i tytuł.
    gameRank = allSpans[indexOfGameRank].get_text(strip=True)                           # allSpans ma wartość zaczynającą się od [1], ponieważ allSpans[0] to numer gry, czyli "1.".
    return gameRank                                                                     # Zbiera miejsce w rankingu gry

def getGameName(indexOfGameName):                                                       # Spany w klasie .c-finderProductCard_titleHeading są dwa: numer i tytuł.
    gameName = allSpans[indexOfGameName].get_text(strip=True)                           # allSpans ma wartość zaczynającą się od [1], ponieważ allSpans[0] to numer gry, czyli "1.".
    return gameName                                                                     # Zwraca nazwę gry.

def getGameRating(indexOfGameRating):                                                   # Zbiera rating.
    gameRating = allRating[indexOfGameRating].get_text(strip=True)
    return gameRating                                                                   # Zwraca rating gry

def getGameYear(indexOfGameYear):                                                       # Zbiera lata
    yearOnly = allYears[indexOfGameYear].get_text(strip=True)
    gameYear = yearOnly.split(',')[-1].strip()                                          # Split dzieli to co w yearOnly wtedy, kiedy natknie się na przecinek, a następnie usuwa spację poprzez strip. Jest to potrzebne, bo data na Metacritic podawana jest z dniami i miesiącami, a chcemy tylko rok.
    return gameYear




pagesToParse = int(input("How many pages you want to parse? "))                         # Definiujemy ile stron będzie parsowane


gamesData = []                                                                          # Definiujemy ogólne gamesData, które zapiszemy całościowo do pliku json.
pageNumber = 1                                                                          # Definiujemy pageNumber, czyli numer strony, która będzie użyta w ścieżce do strony html jaką chcemy przepracować.
pagesParsed = 0


for _ in range (1, pagesToParse + 1):                                                   # Druga liczba, to liczba stron html, jaką chcemy sparsować, według wzoru pagestoParse+1
    with open(f'/home/jakub/Studia/magisterka-badanie/metacritic-scraping/pages/Page{pageNumber}.html', encoding='utf-8') as file:                                                                              # Otwiera 
        soup = BeautifulSoup(file, 'html.parser')                                                                                                                                                               # i parsuje Page.html do zmiennej soup

    allSpans = soup.select('.c-finderProductCard_titleHeading span')                                                                                                                                            # Zbiera wszystkie spany z nazwą gry do zmiennej allSpans
    allRating = soup.select('.c-finderProductCard_score .u-flexbox-row .c-siteReviewScore_background .c-siteReviewScore span')            # Zbiera wszystkie spany z oceną gry do zmiennej allRating
    allYears = soup.select('.c-finderProductCard_meta .u-text-uppercase')                                                                                                                                       # Zbiera wszystkie spany z datą wydania gry do zmiennej allYears

    indexOfGameRank = 0
    indexOfGameName = 1                                                                 # Ustawiamy liczbę dla tych zmiennych, aby później służyły za indexy przy wyciąganiu surowych danych
    indexOfGameRating = 0                                                               #
    indexOfGameYear = 0                                                                 #

    for _ in range(24):                                                                 # Wykonujemy pętle, która uzyska nam wszystkie 24 gry na stronie wraz z rokiem i ratingiem
        try:
            game = {                                                                    # Otwieramy nowy wpis do pliku json, który będzie zawierał
                "name":      getGameName(indexOfGameName),                              # 'name:' 'nazwa gry'                           
                "year":      getGameYear(indexOfGameYear),                              # 'year:' 'rok gry'
                "rating":    getGameRating(indexOfGameRating),                          # 'rating:' 'rating gry'
                "rank":      getGameRank(indexOfGameRank), 
                "available": '' }                                                       # 'available', które przyda się później.
            
            gamesData.append(game)                                                      # Łączymy wszystkie powyższe cztery wartości w jeden wpis game
        except IndexError:
            continue

        indexOfGameRank += 2
        indexOfGameName += 2                                                            # Zwiększamy indexy, dla kolejnych gier.
        indexOfGameRating += 1                                                          #
        indexOfGameYear += 1                                                            #

    pageNumber += 1                                                                     # Zwiększamy pageNumber o 1, żeby móc sparsować dane dla gier na kolejncyh stronach.
    pagesParsed += 1

    with open('gamesData.json', 'w', encoding='utf-8') as f:                            # Otwieramy plik json i zapisujemy w nim dane.
        json.dump(gamesData, f, ensure_ascii=False, indent=4)