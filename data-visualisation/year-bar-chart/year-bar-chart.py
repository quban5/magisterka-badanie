import json
import matplotlib.pyplot as plt
import numpy as np




# Opening the data set
print(f"Provide a path to the main data file:\n")
input_filename = input()
with open(input_filename, 'r', encoding='utf-8') as f:
    data = json.load(f)




# Preparing data structure for counting
ranges = [
    (1995, 2000), (2001, 2005), (2006, 2010), (2011, 2015)
]
stats = {f"{low}-{high}": {"yes": 0, "no": 0} for low, high in ranges}




 # Availability counting in ranges
for item in data:
    if item.get("available") == "prob":
        continue
    year = int(item.get("year", 0))
    available = item.get("available", "no").lower()
         
    for low, high in ranges:
        if low <= year <= high:
            label = f"{low}-{high}"
            if available == "yes":
                stats[label]["yes"] += 1
            else:
                stats[label]["no"] += 1
            break




labels = list(stats.keys())
yes_vals = np.array([stats[label]['yes'] for label in labels])
no_vals = np.array([stats[label]['no'] for label in labels])

fig, ax = plt.subplots(figsize=(12, 7))
width = 0.5

def make_labels(values, total_values):
    labels = []

    for value, total in zip(values, total_values):
        if total == 0:
            labels.append('')
        else:
            percent = value / total * 100
            labels.append(f'{percent:.1f}% ({value})')

    return labels

p1 = ax.bar(labels, yes_vals, width, label='Dostępne', color='#72AC43')
p2 = ax.bar(labels, no_vals, width, bottom=yes_vals, label='Niedostępne', color='#C63F3E')

totals = yes_vals + no_vals
    
ax.bar_label(p1, labels=make_labels(yes_vals, totals), label_type='center', fontweight='regular', color='#272727')
ax.bar_label(p2, labels=make_labels(no_vals, totals), label_type='center', fontweight='regular', color='#272727')

ax.grid(axis='y', linestyle='--', alpha=0.3)
ax.set_ylabel('Liczba gier')
ax.set_xlabel('Przedziały lat')
ax.legend()

plt.tight_layout()
plt.show()
