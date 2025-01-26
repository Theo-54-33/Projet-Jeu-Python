import json
import os

# Définir un chemin de sauvegarde
SAVE_FILE = "game_save.json"

# Exemple de structure de données pour la sauvegarde du jeu
default_game_data = {
    "player_name": "Hero",
    "level": 1,
    "hp": 100,
    "mp": 50,
    "inventory": [],
    "quests_completed": [],
    "location": {"x": 0, "y": 0},
    "equipment": {
        "weapon": "None",
        "armor": "None"
    }
}

# Fonction de sauvegarde
def save_game(data):
    """
    Sauvegarde les données du jeu dans un fichier JSON.
    """
    try:
        with open(SAVE_FILE, "w") as save_file:
            json.dump(data, save_file, indent=4)
        print("Jeu sauvegardé avec succès.")
    except Exception as e:
        print(f"Erreur de sauvegarde: {e}")

# Fonction de chargement
def load_game():
    """
    Charge les données du jeu depuis le fichier JSON.
    """
    if not os.path.exists(SAVE_FILE):
        print("Aucune sauvegarde trouvée. Retour aux paramètres par défaut.")
        return default_game_data

    try:
        with open(SAVE_FILE, "r") as save_file:
            data = json.load(save_file)
        print("Jeu chargé avec succès.")
        return data
    except Exception as e:
        print(f"Erreur de chargement: {e}")
        return default_game_data

# Exemple de test de sauvegarde et de chargement
if __name__ == "__main__":
    # Sauvegarder les données actuelles du jeu
    game_data = {
        "player_name": "Warrior",
        "level": 10,
        "hp": 300,
        "mp": 150,
        "inventory": ["Potion", "Elixir"],
        "quests_completed": ["Save the Princess"],
        "location": {"x": 50, "y": 100},
        "equipment": {
            "weapon": "Excalibur",
            "armor": "Knight's Armor"
        }
    }
    save_game(game_data)

    # Charger les données du jeu
    loaded_game_data = load_game()
    print(loaded_game_data)
