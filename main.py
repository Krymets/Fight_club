import random
from time import sleep
from classes import Hello
from config import *


Hello.hello()
challengers2 = [knight, rascal, hunter, assassin, mage]

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
    print(f'Королівська битва завершена, вітаємо переможця - {winner.name}!')
else:
    print('Добре, можемо і перенести, нічого страшного. Розходьтесь...')
