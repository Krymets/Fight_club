from abc import ABC, abstractmethod
from time import sleep


class Hero(ABC):
    @abstractmethod
    def __init__(self, name, health, armor, power, weapon):
        self.name = name
        self.health = health  # число
        self.armor = armor  # строка
        self.power = power  # число
        self.weapon = weapon  # строка

    def __str__(self):
        return f"Привітайте героя -> {self.name}, Рівень здоров\'я: {self.health}, Клас броні: {self.armor}, " \
               f"Сила удару: {self.power}, Зброя: {self.weapon} \n"

    def battle(self, enemy):
        while self.health and enemy.health > 0:
            self.atack(enemy)
            if enemy.health <= 0:
                print(enemy.name, 'пав у цьому нелегкому бою!\n')
                break
            sleep(5)

            enemy.atack(self)
            if self.health <= 0:
                print(self.name, 'пав у цьому нелегкому бою!\n')
                break
            sleep(5)

    def atack(self, enemy):
        print(
            '-> УДАР! ' + self.name + ' атакує ' + enemy.name
            + ' з силою ' + str(self.power) + ', використовуючи ' + self.weapon + '\n')
        if enemy.armor == 0:
            enemy.health -= self.power
            print(f'{enemy.name} отримав {self.power} урону.\nРівень здоров\'я падає до ' + str(enemy.health) + '\n')
        else:
            enemy.armor -= self.power
            if enemy.armor < 0:
                enemy.health += enemy.armor
                enemy.armor = 0
            print(
                enemy.name + ' покачнувся(-ась).\nКлас броні впав до ' +
                str(enemy.armor) + ', а рівень здоров\'я до ' + str(enemy.health) + '\n')
