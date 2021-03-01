import random

class Hero:
    def __init__(self, name, hit_points):
        self.name = name
        self.hit_points = hit_points

    def attack(self):
        attack_roll = random.randint(1, 20)
        defense_roll = random.randint(1, 20)
        print(f"{self.name} attacks and rolls a {attack_roll}")
        print(f"the opponent rolls a {defense_roll}")
        if attack_roll >= defense_roll:
            print(f"{self.name} hits his opponent")
        else:
            print(f"The opponent block the attack")

Kyle = Hero("kyle", 1)
Kyle.attack()