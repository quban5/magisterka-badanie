import matplotlib.pyplot as plt
import json

#Load the json file
with open('/home/jakub/Studia/magisterka-badanie/data-visualisation/gamesDataForVisualization.json', 'r', encoding='utf-8') as f:
    gamesData = json.load(f)

names = [game["name"] for game in gamesData]
availability = [game["available"] for game in gamesData]

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

labels = ['Available (Yes)', 'Not Available (No)']
sizes = [yesCount, noCount]
colors = ['green', 'red']

plt.figure(figsize=(6, 6))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, startangle=140)
plt.title('Game Availability on PC (Pie Chart)')
plt.axis('equal')  # Keeps circle shape
plt.tight_layout()
plt.show()