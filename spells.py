# spells.py
class Spell:
    def __init__(self, name, mp_cost, power, description):
        self.name = name
        self.mp_cost = mp_cost
        self.power = power
        self.description = description

    def cast(self, caster, target):
        """Lance un sort du caster sur la cible."""
        if caster.mp >= self.mp_cost:
            caster.mp -= self.mp_cost
            print(f"{caster.name} utilise {self.name}!")
            target.take_damage(self.power)
        else:
            print(f"{caster.name} n'a pas assez de MP pour utiliser {self.name}!")

# Sorts de type Feu
class FireSpell(Spell):
    def __init__(self, name, mp_cost, power):
        description = f"Inflige {power} points de dégâts de feu."
        super().__init__(name, mp_cost, power, description)

class FireExtraSpell(FireSpell):
    def __init__(self):
        super().__init__("Feu Extra", 20, 150)

class FireMegaSpell(FireSpell):
    def __init__(self):
        super().__init__("Feu Mega", 40, 300)

class FireUltimeSpell(FireSpell):
    def __init__(self):
        super().__init__("Feu Ultime", 60, 500)

# Sorts de type Glace
class IceSpell(Spell):
    def __init__(self, name, mp_cost, power):
        description = f"Inflige {power} points de dégâts de glace."
        super().__init__(name, mp_cost, power, description)

class IceExtraSpell(IceSpell):
    def __init__(self):
        super().__init__("Glace Extra", 25, 180)

class IceMegaSpell(IceSpell):
    def __init__(self):
        super().__init__("Glace Mega", 45, 350)

class IceUltimeSpell(IceSpell):
    def __init__(self):
        super().__init__("Glace Ultime", 70, 600)

# Sorts de soin
class HealSpell(Spell):
    def __init__(self, name, mp_cost, healing_amount):
        description = f"Soigne {healing_amount} points de vie."
        super().__init__(name, mp_cost, healing_amount, description)

class HealExtraSpell(HealSpell):
    def __init__(self):
        super().__init__("Soin Extra", 15, 200)

class HealMegaSpell(HealSpell):
    def __init__(self):
        super().__init__("Soin Mega", 30, 400)

class HealUltimeSpell(HealSpell):
    def __init__(self):
        super().__init__("Soin Ultime", 50, 700)
