# battle.py
class Battle:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def start_battle(self):
        """Démarre le combat entre le joueur et l'ennemi."""
        print(f"{self.player.name} affronte {self.enemy.name}!")
        while self.player.hp > 0 and self.enemy.hp > 0:
            self.player_turn()
            if self.enemy.hp > 0:
                self.enemy_turn()
        if self.player.hp <= 0:
            print(f"{self.player.name} est tombé au combat!")
            self.end_battle(False)
        else:
            print(f"{self.enemy.name} a été vaincu!")
            self.end_battle(True)

    def player_turn(self):
        """Tour du joueur."""
        print("Que voulez-vous faire ?")
        print("1. Attaquer")
        print("2. Utiliser un sort")
        choice = input("Choix: ")

        if choice == "1":
            self.player.attack_enemy(self.enemy)
        elif choice == "2":
            self.use_player_spell()

    def use_player_spell(self):
        """Le joueur utilise un sort."""
        print("Quels sorts voulez-vous utiliser ?")
        for i, spell in enumerate(self.player.spells):
            print(f"{i+1}. {spell.name} - {spell.description}")

        choice = int(input("Choix du sort: ")) - 1
        if 0 <= choice < len(self.player.spells):
            spell = self.player.spells[choice]
            self.player.cast_spell(spell, self.enemy)
        else:
            print("Sort invalide.")

    def enemy_turn(self):
        """Tour de l'ennemi."""
        print(f"{self.enemy.name} attaque !")
        damage = self.enemy.attack
        self.player.take_damage(damage)

    def end_battle(self, player_wins):
        """Fin du combat."""
        if player_wins:
            print("Vous avez gagné le combat !")
        else:
            print("Game Over. Vous avez perdu.")
