# player.py
class Player:
    def __init__(self, name, hp, mp, attack, defense):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.mp = mp
        self.max_mp = mp
        self.attack = attack
        self.defense = defense
        self.position = [0, 0]  # Position sur la carte
        self.spells = []  # Liste des sorts disponibles

    def learn_spell(self, spell):
        """Apprend un nouveau sort."""
        self.spells.append(spell)
        print(f"{self.name} a appris {spell.name}!")

    def cast_spell(self, spell, target):
        """Le joueur utilise un sort."""
        if spell in self.spells:
            spell.cast(self, target)
        else:
            print(f"{self.name} ne connaît pas ce sort.")

    def take_damage(self, damage):
        """Le joueur prend des dégâts."""
        self.hp -= max(0, damage - self.defense)
        if self.hp <= 0:
            self.die()

    def heal(self, amount):
        """Le joueur se soigne."""
        self.hp = min(self.max_hp, self.hp + amount)

    def die(self):
        """Le joueur meurt."""
        print(f"{self.name} est mort!")
        return False

    def attack_enemy(self, enemy):
        """Le joueur attaque un ennemi."""
        print(f"{self.name} attaque {enemy.name}!")
        damage = self.attack
        enemy.take_damage(damage)
