import json
import matplotlib.pyplot as plt
import numpy as np




print(f"Provide a path to the main data file:\n")
input_filename = input()
with open(input_filename, 'r', encoding='utf-8') as f:
    data = json.load(f)




ranges = [
    (91, 100), (81, 90), (71, 80), (61, 70), (51, 60), (41, 50), (31, 40), (21, 30), (11, 20)
]
stats = {f"{low}-{high}": {"yes": 0, "no": 0} for low, high in ranges}




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

colors = {'Dostępne': '#72AC43', 'Niedostępne': '#C63F3E'}
width = 0.6

# 3 subploty obok siebie
for i in range(3):

    fig, ax = plt.subplots(figsize=(6, 6))

    # Fragment danych
    chunk_labels = labels[i*3 : (i+1)*3]
    chunk_yes = yes_vals[i*3 : (i+1)*3]
    chunk_no = no_vals[i*3 : (i+1)*3]

    # Skumulowane słupki
    p1 = ax.bar(
        chunk_labels,
        chunk_yes,
        width,
        label='Dostępne',
        color=colors['Dostępne']
    )

    p2 = ax.bar(
        chunk_labels,
        chunk_no,
        width,
        bottom=chunk_yes,
        label='Niedostępne',
        color=colors['Niedostępne']
    )

    # Etykiety
    totals = chunk_yes + chunk_no

    def make_labels(values, total_values):
        labels = []

        for value, total in zip(values, total_values):
            if total == 0:
                labels.append('')
            else:
                percent = value / total * 100
                labels.append(f'{percent:.1f}% ({value})')

        return labels

    ax.bar_label(
        p1,
        labels=make_labels(chunk_yes, totals),
        label_type='center',
        fontweight='regular',
        color='#272727'
    )

    ax.bar_label(
        p2,
        labels=make_labels(chunk_no, totals),
        label_type='center',
        fontweight='regular',
        color='#272727'
    )

    # Tytuł wykresu
    if i == 0:
        ax.set_title('Rating od 100 do 71', fontsize=14)
    elif i == 1:
        ax.set_title('Rating od 70 do 41', fontsize=14)
    else:
        ax.set_title('Rating od 40 do 11', fontsize=14)

    ax.grid(axis='y', linestyle='--', alpha=0.3)

    ax.legend()
    ax.set_ylabel('Liczba gier')
    ax.set_xlabel('Przedziały ratingu')

    plt.tight_layout()

    # Każdy wykres jako osobny obraz
    plt.savefig(
        f'rating-bar-chart-{i+1}.png',
        dpi=300,
        bbox_inches='tight'
    )

    plt.show()
    plt.close(fig)
