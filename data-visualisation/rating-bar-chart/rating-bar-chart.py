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
    (91, 100), (81, 90), (71, 80), (61, 70), (51, 60), (41, 50), (31, 40), (21, 30), (11, 20)
]
stats = {f"{low}-{high}": {"yes": 0, "no": 0} for low, high in ranges}




 # Availability counting in ranges
for item in data:
    if item.get("available") == "prob":
        continue
    rating = int(item.get("rating", 0))
    available = item.get("available", "no").lower()
            
    for low, high in ranges:
        if low <= rating <= high:
            label = f"{low}-{high}"
            if available == "yes":
                stats[label]["yes"] += 1
            else:
                stats[label]["no"] += 1
            break



labels = list(stats.keys())
yes_vals = np.array([stats[label]['yes'] for label in labels])
no_vals = np.array([stats[label]['no'] for label in labels])

colors = {'Dostępne': '#4CAF50', 'Niedostępne': '#F44336'}
width = 0.6

# Tworzymy 3 subploty obok siebie (1 wiersz, 3 kolumny)
fig, axes = plt.subplots(1, 3, figsize=(18, 6))

# Pętla przez 3 subploty
for i in range(3):
    ax = axes[i]
    
    # Wybieramy fragment danych (po 3 przedziały na każdy wykres)
    # i*3 : (i+1)*3 daje nam indeksy: [0:3], [3:6], [6:9]
    chunk_labels = labels[i*3 : (i+1)*3]
    chunk_yes = yes_vals[i*3 : (i+1)*3]
    chunk_no = no_vals[i*3 : (i+1)*3]
    
    # Rysujemy skumulowane słupki
    p1 = ax.bar(chunk_labels, chunk_yes, width, label='Dostępne', color=colors['Dostępne'])
    p2 = ax.bar(chunk_labels, chunk_no, width, bottom=chunk_yes, label='Niedostępne', color=colors['Niedostępne'])
    
    # Dodajemy etykiety (liczby) wewnątrz słupków
    ax.bar_label(p1, label_type='center', fontweight='regular', color='#272727')
    ax.bar_label(p2, label_type='center', fontweight='regular', color='#272727')
    

    # Personalizacja każdego subplota
    if i == 0:
        ax.set_title('Rating od 100 do 71', fontsize=14)
    elif i == 1:
        ax.set_title('Rating od 70 do 41', fontsize=14)
    else:
        ax.set_title('Rating od 40 do 11', fontsize=14)


    ax.grid(axis='y', linestyle='--', alpha=0.3)
    

    if i == 0:
        ax.legend()
        ax.set_ylabel('Liczba gier')

plt.tight_layout()
plt.savefig('rating-bar-chart.png', dpi=300, bbox_inches='tight')
plt.show()