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

yesCountPercent = yesCount / len(availability) * 100
noCountPercent = noCount / len(availability) * 100

print("Yes:", yesCount, f"{yesCountPercent} %")
print("No:", noCount, f"{noCountPercent} %")

labels = ['Available', 'Not Available']
sizes = [yesCount, noCount]
colors = ['#39521f', '#ba1b18']

plt.figure(figsize=(6, 6))
plt.pie(sizes, labels=labels, colors=colors, startangle=140)
plt.title('Availability of PC video games (1958-2015) listed on Metacritic')
plt.axis('equal')  # Keeps circle shape
plt.tight_layout()
plt.show()