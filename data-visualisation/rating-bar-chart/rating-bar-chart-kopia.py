import json
import matplotlib.pyplot as plt
import numpy as np

print(f"Provide a path to the main data file:\n")
input_filename = input()

def generate_rating_charts(input_filename):
    # 1. Wczytanie danych
    try:
        with open(input_filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
    except Exception as e:
        print(f"Błąd podczas wczytywania pliku: {e}")
        return

    # 2. Definicja przedziałów
    ranges = [
        (91, 100), (81, 90), (71, 80), (61, 70),
        (51, 60), (41, 50), (31, 40), (21, 30), (11, 20)
    ]

    # Przygotowanie struktury danych do zliczania: { "91-100": {"yes": 0, "no": 0}, ... }
    stats = {f"{low}-{high}": {"yes": 0, "no": 0} for low, high in ranges}

    # 3. Zliczanie dostępności w przedziałach
    for item in data:
        try:
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
        except (ValueError, TypeError):
            continue

    # 4. Tworzenie wykresów (Siatka 3x3 dla 9 przedziałów)
    fig, axes = plt.subplots(3, 3, figsize=(15, 12))
    axes = axes.flatten() # Spłaszczenie macierzy wykresów do łatwiejszej iteracji
    
    fig.suptitle('Dostępność gier w danych przedziałach', fontsize=20, fontweight='regular', y=0.95)

    for i, (range_name, count_dict) in enumerate(stats.items()):
        ax = axes[i]
        categories = ['Dostępne (yes)', 'Niedostępne (no)']
        values = [count_dict['yes'], count_dict['no']]
        colors = ['#4CAF50', '#F44336'] # Zielony i Czerwony

        bars = ax.bar(categories, values, color=colors, edgecolor='black', alpha=0.8)
        
        # Dodanie etykiet z liczbami nad słupkami
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height + 0.1,
                    f'{int(height)}', ha='center', va='bottom', fontsize=10, fontweight='bold')

        ax.set_title(f"Rating: {range_name}", fontsize=13, pad=10)
        ax.set_ylim(0, max(values) * 1.2 if max(values) > 0 else 10) # Dynamiczna wysokość osi Y
        ax.grid(axis='y', linestyle='--', alpha=0.6)

    # Układanie elementów i zapis/wyświetlenie
    plt.tight_layout(rect=[0, 0.03, 1, 0.92])
    plt.savefig('statystyki_dostepnosci.png', dpi=300)
    print("Wykres został zapisany jako 'statystyki_dostepnosci.png'")
    plt.show()

if __name__ == "__main__":
    # Upewnij się, że nazwa pliku zgadza się z Twoim plikiem wejściowym
    generate_rating_charts(input_filename)