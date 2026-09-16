import matplotlib.pyplot as plt
import json

print(f"Provide a path to the main data file:\n")
pathToFile = input()
with open(pathToFile, 'r', encoding='utf-8') as f:
    gamesData = json.load(f)

availability = [game["available"] for game in gamesData] # Grabs all "available" strings and makes a list

yesCount = 0
noCount = 0

for available in availability:
    if available == "yes":
        yesCount += 1
    elif available == "no":
        noCount += 1

totalCount = yesCount + noCount

yesCountPercent = yesCount / totalCount * 100
noCountPercent = noCount / totalCount * 100

print('Yes:', yesCount, f"{yesCountPercent} %")
print('No:', noCount, f"{noCountPercent} %")

labels = ['Dostępne', 'Niedostępne']
sizes = [yesCount, noCount]
colors = ['#72AC43', '#C63F3E']

def make_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        count = int(round(pct * total / 100.0))
        return f'{pct:.1f}% ({count})'
    return my_autopct

plt.figure(figsize=(6, 6))
plt.pie(sizes, labels=labels, colors=colors, startangle=140, autopct=make_autopct(sizes), pctdistance=0.79, textprops={'color': 'black', 'fontsize': 12}, wedgeprops={"width": 0.4, "edgecolor": "white"})
plt.axis('equal')
plt.tight_layout()
plt.show()
