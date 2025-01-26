import os
import datetime
import traceback
import time
import pygame  # Assurez-vous que pygame est installé

# Importation des fichiers du jeu
import player
import enemy
import battle
import game
import spells

# Créer un dossier pour les logs si il n'existe pas
LOG_DIR = "game_logs"
LOG_FILE = os.path.join(LOG_DIR, "game_log.txt")

if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)
    print(f"Dossier des logs créé : {LOG_DIR}")

# Fonction pour ajouter des événements dans le fichier de log
def log_event(message):
    """
    Enregistre un événement dans le fichier de log avec horodatage.
    """
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as log_file:
        log_file.write(f"[{timestamp}] {message}\n")
    print(f"Événement enregistré dans le log : {message}")

# Fonction pour démarrer le jeu
def start_game():
    """
    Démarre le jeu en enregistrant un message dans le log et lance la boucle principale du jeu.
    """
    try:
        log_event("Le jeu a démarré.")
        
        # Initialiser pygame
        pygame.init()

        # Paramètres de la fenêtre du jeu
        screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Mon Jeu RPG")
        
        # Affichage du menu principal
        show_main_menu(screen)

        # Démarrer la boucle principale du jeu après le menu
        game_running = True
        while game_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:  # Touche 'Q' pour quitter
                        game_running = False
                    elif event.key == pygame.K_s:  # Touche 'S' pour commencer le jeu
                        log_event("Début du jeu.")
                        game_running = False

            pygame.display.flip()

        # Charger le jeu après avoir appuyé sur 'S'
        load_game()

        # Démarrer un combat après avoir chargé le jeu
        start_battle()

    except Exception as e:
        log_event(f"Erreur lors du lancement du jeu : {str(e)}")
        log_event(f"Traceback : {traceback.format_exc()}")

# Fonction pour afficher le menu principal
def show_main_menu(screen):
    """
    Affiche le menu principal du jeu.
    """
    font = pygame.font.Font(None, 48)
    title_text = font.render("Bienvenue dans le Jeu RPG", True, (255, 255, 255))
    start_text = font.render("Appuyez sur 'S' pour commencer", True, (255, 255, 255))
    quit_text = font.render("Appuyez sur 'Q' pour quitter", True, (255, 255, 255))

    screen.fill((0, 0, 0))  # Remplir l'écran avec la couleur noire
    screen.blit(title_text, (200, 150))
    screen.blit(start_text, (200, 250))
    screen.blit(quit_text, (200, 350))
    pygame.display.flip()

    log_event("Menu principal affiché.")

# Fonction pour charger la sauvegarde (simulation)
def load_game():
    """
    Simule le chargement de la sauvegarde du jeu.
    """
    log_event("Chargement des données du jeu...")
    time.sleep(1)
    log_event("Sauvegarde chargée avec succès.")
    
    # Exemple de chargement d'un joueur et d'un ennemi
    player_data = player.Player(name="Héros", hp=100, attack=20, defense=10)
    enemy_data = enemy.Enemy(name="Goblin", hp=50, attack=10, defense=5)
    log_event(f"Joueur chargé : {player_data.name}")
    log_event(f"Ennemi chargé : {enemy_data.name}")
    
    return player_data, enemy_data

# Fonction pour démarrer un combat (simulation)
def start_battle():
    """
    Simule le démarrage d'un combat dans le jeu.
    """
    log_event("L'ennemi apparaît ! Préparez-vous à combattre.")
    
    # Exemple de combat avec un sort
    spell = spells.Fireball()
    log_event(f"Le joueur utilise le sort {spell.name}.")
    time.sleep(2)
    log_event("Combat terminé. Victoire du joueur.")

# Fonction principale - Lance le jeu et enregistre les événements
if __name__ == "__main__":
    log_event("Lancement du jeu via launcher.py.")
    start_game()
    log_event("Fin du processus de lancement du jeu.")
