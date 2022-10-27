
from hero_classes_pack.hero_classes import Hero


class Assassin(Hero):
    def __init__(self, name, health, armor, power, weapon):
        super().__init__(name, health, armor, power, weapon)

    def __str__(self):
        return f"Із натовпу виходить {self.name}, з його рукавів виглядають {self.weapon}\n"

    def atack(self, enemy):
        print(f'>>> [БРОСОК] {self.name} робить випад і кидає {self.weapon} в {enemy.name}\n')
        if enemy.armor == 0:
            enemy.health -= self.power
            print(f'{enemy.name} отримав {self.power} урону.\nРівень здоров\'я падає до ' + str(enemy.health) + '\n')
        else:
            enemy.armor -= self.power
            if enemy.armor < 0:
                enemy.health += enemy.armor
                enemy.armor = 0
            print(f'{enemy.name} не встиг ухилитися...\n'
                  f'Тепер його броня: {enemy.armor}, а рівень здоров\'я: {enemy.health}\n')
