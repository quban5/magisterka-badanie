import json

print(f"Provide a path to the main data file:\n")
pathToFile = input()

with open(pathToFile, 'r', encoding='utf-8') as f:
    data = json.load(f)

ranges = [
        (91, 100), (81, 90), (71, 80), (61, 70), (51, 60), (41, 50), (31, 40), (21, 30), (11, 20)
]

binnedData = {f"{low}-{high}": [] for low, high in ranges}
others = []

for item in data:
        try:
            rating = int(item.get("rating", 0))
            
            foundRange = False
            for low, high in ranges:
                if low <= rating <= high:
                    binnedData[f"{low}-{high}"].append(item)
                    foundRange = True
                    break
            
            if not foundRange:
                others.append(item)
        except ValueError:
            print(f"{item.get('name')}: not valid rating value")

for rangeName, items in binnedData.items():
        if items:
            output_filename = f"games_rating_{rangeName}.json"
            with open(output_filename, 'w', encoding='utf-8') as out_file:
                json.dump(items, out_file, indent=4, ensure_ascii=False)
            print(f"Created file: {output_filename} ({len(items)} items)")

if others:
        with open("games_rating_others.json", "w", encoding="utf-8") as out_file:
            json.dump(others, out_file, indent=4, ensure_ascii=False)
        print(f"Created file: games_rating_others.json ({len(others)} items)")