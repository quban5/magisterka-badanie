import json

# Load the JSON file
with open('/home/jakub/Studia/magisterka-badanie/data-reviewing/gamesData.json', 'r', encoding='utf-8') as f:
    games = json.load(f)

# Get total number of unanswered entries
total_remaining = sum(1 for g in games if g.get("available", "") == "")
current_index = 1

# Loop through each game where "available" is still empty
for game in games:
    if game.get("available", "") == "":
        print(f"\nGame: {game['name']}")
        while True:
            prompt = f"[{current_index} / {total_remaining}] Is it available? (y/n or 'exit'): "
            user_input = input(prompt).strip().lower()
            if user_input == 'y':
                game["available"] = "yes"
                break
            elif user_input == 'n':
                game["available"] = "no"
                break
            elif user_input == 'exit':
                with open('/home/jakub/Studia/magisterka-badanie/data-reviewing/gamesData.json', 'w', encoding='utf-8') as f:
                    json.dump(games, f, ensure_ascii=False, indent=4)
                print("\nProgress saved. Exiting.")
                exit()
            else:
                print("Please type 'y', 'n', or 'exit'.")
        current_index += 1

# Final save
with open('/home/jakub/Studia/magisterka-badanie/data-reviewing/gamesData.json', 'w', encoding='utf-8') as f:
    json.dump(games, f, ensure_ascii=False, indent=4)

print("\nAll entries completed and saved.")