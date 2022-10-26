import random
from abc import ABC, abstractmethod
from time import sleep


# class Hero(ABC):
#     @abstractmethod
class Hero:
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


knight = Hero('Лицар Річард "Гострий меч"', 50, 25, 20, 'меч')  # name, health, armor, power, weapon
rascal = Hero('Пройдисвіт Петро "Підступний ніж"', 95, 5, 7, 'ніж')
hunter = Hero('Мисливець Хантер "Довгий лук"', 70, 10, 15, 'лук')
assassin = Hero('Вбивця Эціо "Друг Леонардо Да Вінчі"', 70, 3, 20, 'метальні ножі')
mage = Hero('Маг Гендальф "Білий"', 85, 0, 16, 'посох')

print('Вітаємо сьогоднішніх претендентів кубку короля')

challengers = [knight, rascal, hunter, assassin, mage]
challengers2 = [knight, rascal, hunter, assassin, mage]

print(knight.__str__())
print(rascal.__str__())
print(assassin.__str__())
print(hunter.__str__())
print(mage.__str__())

sleep(5)
if input('Наступає час початку битви і король має дати команду починати битву (так / ні) >>> ').lower() == 'так':
    print('\nНехай Королівська битва почнеться!\n')
    fight_round = 1
    sleep(3)
    print('Приберіть арену!\n')
    while len(challengers) > 1:
        sleep(3)
        print(f'Починається {fight_round} поєдинок!\n')
        sleep(5)
        first_fighter = random.choice(challengers)
        challengers2.remove(first_fighter)
        second_fiter = random.choice(challengers2)
        challengers2 = challengers
        print(f'Зустрічаються: {first_fighter.name} та {second_fiter.name}! \nПобажаємо їм успіху! До бою!\n')
        sleep(4)
        first_fighter.battle(second_fiter)
        if first_fighter.health <= 0:
            print(f'Вітаємо переможця поєдинку, це {second_fiter.name}! Він іде відновлювати сили під ваші оплески.')
            sleep(3)
            print(f'{first_fighter.name} нажаль вибуває, приберіть арену для наступного поєдинку.')
            winner = second_fiter
            challengers.remove(first_fighter)
        else:
            print(f'Вітаємо переможця поєдинку, це {first_fighter.name}! Він іде відновлювати сили під ваші оплески.')
            sleep(3)
            print(f'{second_fiter.name} нажаль вибуває.')
            winner = first_fighter
            challengers.remove(second_fiter)
        fight_round += 1
        if winner.name == knight.name:
            knight.health, knight.armor, knight.power = 50, 25, 20
        elif winner.name == rascal.name:
            rascal.health, rascal.armor, rascal.power = 20, 5, 5
        elif winner.name == hunter.name:
            hunter.health, hunter.armor, hunter.power = 80, 10, 15
        elif winner.name == assassin.name:
            assassin.health, assassin.armor, assassin.power = 70, 3, 20
        elif winner.name == mage.name:
            mage.health, mage.armor, mage.power = 100, 0, 16
    print(f'Королівська битва завершена, вітаємо {winner.name}!')
else:
    print('Добре, можемо і перенести, нічого страшного. Розходьтесь...')
