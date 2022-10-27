
from hero_classes_pack.hero_classes import Hero


class Rascal(Hero):
    def __init__(self, name, health, armor, power, weapon):
        super().__init__(name, health, armor, power, weapon)

    def __str__(self):
        return f"Мов хитрий лис, виходить {self.name}, від посміхається гнилими зубами і направляє свій {self.weapon} " \
               f"у напрямку судей\n"

    def atack(self, enemy):
        print(f'>>> [УДАР] {self.name} замахується і ріже обличчя {enemy.name} своїм {self.weapon}ем \n')
        if enemy.armor == 0:
            enemy.health -= self.power
            print(f'{enemy.name} корчиться від болю, він отримав {self.power} урону.\nРівень здоров\'я падає '
                  f'до {enemy.health}\n')
        else:
            enemy.armor -= self.power
            if enemy.armor < 0:
                enemy.health += enemy.armor
                enemy.armor = 0
            print(f'{enemy.name} плаче від болю\n'
                  f'Тепер його броня: {enemy.armor}, а рівень здоров\'я: {enemy.health}\n')
