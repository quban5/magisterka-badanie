from bs4 import BeautifulSoup
import json


# Spany w klasie .c-finderProductCard_titleHeading są dwa: numer i tytuł.
# allSpans ma wartość zaczynającą się od [1], ponieważ allSpans[0] to numer gry, czyli "1."
def getGameName(indexOfGameName):
    gameName = allSpans[indexOfGameName].get_text(strip=True)
    return gameName

# Zbiera rating
def getGameRating(indexOfGameRating):
    gameRating = allRating[indexOfGameRating].get_text(strip=True)
    return gameRating

# Zbiera lata
def getGameYear(indexOfGameYear):
    yearOnly = allYears[indexOfGameYear].get_text(strip=True)
    # Split dzieli to co w yearOnly wtedy, kiedy natknie się na przecinek,
    # a następnie usuwa spację poprzez strip.
    # Jest to potrzebne, bo data na Metacritic podawana jest z dniami i miesiącami, a chcemy tylko rok.
    gameYear = yearOnly.split(',')[-1].strip()
    return gameYear


# Definiujemy ogólne gamesData, które zapiszemy całościowo do pliku json
gamesData = []

# Definiujemy pageNumber, czyli numer strony, która będzie użyta w ścieżce do strony html
# jaką chcemy przepracować
pageNumber = 1


for _ in range (1, 6): # Druga liczba, to liczba stron html, jaką chcemy sparsować, według wzoru n+1

    #Otwiera i parsuje Page.html do zmiennej soup
    with open(f'/home/jakub/Studia/magisterka-badanie/metacritic-scraping/pages/Page{pageNumber}.html', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')

    # Zbiera wszystkie spany z nazwą gry do zmiennej allSpans
    # Zbiera wszystkie spany z oceną gry do zmiennej allRating
    # Zbiera wszystkie spany z datą wydania gry do zmiennej allYears
    allSpans = soup.select('.c-finderProductCard_titleHeading span')
    allRating = soup.select('div.c-siteReviewScore.u-flexbox-column.u-flexbox-alignCenter.u-flexbox-justifyCenter.g-text-bold.c-siteReviewScore_green.g-color-gray90.c-siteReviewScore_xsmall span')
    allYears = soup.select('.c-finderProductCard_meta .u-text-uppercase')

    # Ustawiamy liczbę dla tych zmiennych, aby później służyły za indexy
    indexOfGameName = 1
    indexOfGameRating = 0
    indexOfGameYear = 0

    # Wykonujemy pętle, która uzyska nam wszystkie 24 gry na stronie wraz z rokiem i ratingiem
    for _ in range(24):
        try:
            game = {
                "name":      getGameName(indexOfGameName),    # Otwieramy nowy wpis do pliku json, który będzie zawierał
                "year":      getGameYear(indexOfGameYear),    # 'name:' 'nazwa gry', 'year:' 'rok gry', 'rating:' 'rating gry'
                "rating":    getGameRating(indexOfGameRating),
                "available": '' }
            
            gamesData.append(game)  # Łączymy wszystkie powyższe cztery wartości w jeden wpis game
        except IndexError:
            continue

        indexOfGameName += 2    # Zwiększamy indexy, do kolejnych gier
        indexOfGameRating += 1
        indexOfGameYear += 1

    pageNumber += 1


# Otwieramy i zapisujemy dane w pliku json
with open('gamesData.json', 'w', encoding='utf-8') as f:
    json.dump(gamesData, f, ensure_ascii=False, indent=4)