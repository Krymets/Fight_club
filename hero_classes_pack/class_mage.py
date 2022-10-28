
from hero_classes_pack.hero_classes import Hero


class Mage(Hero):
    def __init__(self, name, health, armor, power, weapon):
        super().__init__(name, health, armor, power, weapon)

    def __str__(self):
        return f"Раптово з\'являється {self.name}, з {self.weapon}ом за спиною\n"

    def atack(self, enemy):
        print(f'>>> [ЗАКЛЯТТЯ] {self.name} проклинає {enemy.name} і б\'є {self.weapon}ом на {self.power}\n')
        if not enemy.armor:
            enemy.health -= self.power
            print(f'{enemy.name} отримав {self.power} урону.\nРівень здоров\'я падає до ' + str(enemy.health) + '\n')
        else:
            enemy.armor -= self.power
            if enemy.armor < 0:
                enemy.health += enemy.armor
                enemy.armor = 0
            print(f'Складне заклинання приголомшило {enemy.name}\n'
                  f'Тепер його броня: {enemy.armor}, а рівень здоров\'я: {enemy.health}\n')
