
from hero_classes_pack.hero_classes import Hero


class Hunter(Hero):
    def __init__(self, name, health, armor, power, weapon):
        super().__init__(name, health, armor, power, weapon)

    def __str__(self):
        return f"З'являється {self.name}, з тушею кабана на плечі, із-за спини виглядає {self.weapon}\n"

    def atack(self, enemy):
        print(f'>>> [ПОСТРІЛ] {self.name} сильно натягує тятиву свого {self.weapon}а та '
              f'випускає стрілу у напрямку {enemy.name}\n')
        if not enemy.armor:
            enemy.health -= self.power
            print(f'Стріла влучає в {enemy.name} та наносить {self.power} урону.\nРівень здоров\'я падає '
                  f'до {enemy.health}\n')
        else:
            enemy.armor -= self.power
            if enemy.armor < 0:
                enemy.health += enemy.armor
                enemy.armor = 0
            print(f'{enemy.name} прибило до стіни\n'
                  f'Тепер його броня: {enemy.armor}, а рівень здоров\'я: {enemy.health}\n')
