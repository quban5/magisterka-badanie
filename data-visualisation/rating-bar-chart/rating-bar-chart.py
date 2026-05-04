import json
import matplotlib as plt

print(f"Provide a path to the main data file:\n")
pathToFile = input()
with open(pathToFile, 'r', encoding='utf-8') as f:
    gamesData = json.load(f)