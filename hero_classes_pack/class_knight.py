
from hero_classes_pack.hero_classes import Hero


class Knight(Hero):
    def __init__(self, name, health, armor, power, weapon):
        super().__init__(name, health, armor, power, weapon)

    def __str__(self):
        return f"На арену виходить {self.name}, тримаючи свій {self.weapon} перед собою\n"

    def atack(self, enemy):
        print(f'>>> [УДАР] Хоробрий воїн {self.name} атакує {enemy.name} {self.weapon}ем з силою {self.power}\n')
        if not enemy.armor:
            enemy.health -= self.power
            print(f'{enemy.name} отримав {self.power} урону.\nРівень здоров\'я падає до ' + str(enemy.health) + '\n')
        else:
            enemy.armor -= self.power
            if enemy.armor < 0:
                enemy.health += enemy.armor
                enemy.armor = 0
            print(f'Сильний удар збив з ніг {enemy.name}\n'
                  f'Тепер його броня: {enemy.armor}, а рівень здоров\'я: {enemy.health}\n')
