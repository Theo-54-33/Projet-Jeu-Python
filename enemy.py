# enemy.py
class Enemy:
    def __init__(self, name, hp, mp, attack, defense):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.mp = mp
        self.max_mp = mp
        self.attack = attack
        self.defense = defense

    def take_damage(self, damage):
        """L'ennemi prend des dégâts."""
        self.hp -= max(0, damage - self.defense)
        if self.hp <= 0:
            self.die()

    def die(self):
        """L'ennemi meurt."""
        print(f"{self.name} est vaincu!")

    def attack_player(self, player):
        """L'ennemi attaque le joueur."""
        print(f"{self.name} attaque {player.name}!")
        damage = self.attack
        player.take_damage(damage)
