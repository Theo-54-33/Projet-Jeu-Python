# game.py
from player import Player
from enemy import Enemy
from spells import FireExtraSpell, FireMegaSpell, IceExtraSpell, HealExtraSpell
from battle import Battle

def main():
    # Créer un joueur
    player = Player("Héros", 1000, 200, 150, 50)

    # Le joueur apprend des sorts
    fire_spell = FireExtraSpell()
    player.learn_spell(fire_spell)

    ice_spell = IceExtraSpell()
    player.learn_spell(ice_spell)

    heal_spell = HealExtraSpell()
    player.learn_spell(heal_spell)

    # Créer un ennemi
    enemy = Enemy("Dragon", 500, 100, 50, 30)

    # Lancer un combat
    battle = Battle(player, enemy)
    battle.start_battle()

if __name__ == "__main__":
    main()
