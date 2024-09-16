class Warrior():
    def __init__(self, name, health, attack_power, energy):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.energy = energy

    def sleep(self):
        print(f'{self.name} sleep')
        self.health += 50

    def attack(self, enemy):
        print(f'{self.name} attacks {enemy.name}')
        enemy.health -= self.attack_power
        self.energy -= 5

    def eat(self):
        print(f'{self.name} eats')
        self.health += 20
        self.energy += 10
        if self.health > 100:
            self.health = 100
        if self.energy > 100:
            self.energy = 100

    def info(self):
        print(f'имя воина {self.name},энергия - {self.energy}, сила воина - {self.attack_power}, здоровье воина - {self.health}))



