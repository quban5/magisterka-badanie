# DO DOKOŃCZENIA

import json

print(f"Provide a path to the main data file:\n")
pathToFile = input()

with open(pathToFile, 'r', encoding='utf-8') as f:
    data = json.load(f)

# 1995 - 2000
# 2001 - 2005
# 2006 - 2010
# 2011 - 2015
ranges = [
        (1995, 2000), (2001, 2005), (2006, 2010), (2011, 2015)
]

binnedData = {f"{low}-{high}": [] for low, high in ranges}

for item in data:
    year = int(item.get("year", 0))
            
    for low, high in ranges:
        if low <= year <= high:
            binnedData[f"{low}-{high}"].append(item)
            foundRange = True
            break

for rangeName, items in binnedData.items():
    if items:
        output_filename = f"games_rating_{rangeName}.json"
        with open(output_filename, 'w', encoding='utf-8') as out_file:
            json.dump(items, out_file, indent=4, ensure_ascii=False)
        print(f"Created file: {output_filename} ({len(items)} items)")