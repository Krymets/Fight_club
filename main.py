import random
from time import sleep
from classes import Hello
from config import *

Hello.hello()
if Hello.yes_no() == 'так':
    print('\nНехай Королівська битва почнеться!\n')
    fight_round = 1
    while len(challengers) > 1:
        sleep(2)
        print(f'На арену виходить {len(challengers)} участників')
        sleep(3)
        if len(challengers) == 2:
            print(f'Починається {fight_round} поєдинок!\n Фінальний!')
        else:
            print(f'Починається {fight_round} поєдинок!\n')
        sleep(5)
        first_fighter = random.choice(challengers)
        challengers.remove(first_fighter)
        second_fiter = random.choice(challengers)
        challengers.append(first_fighter)
        print(f'Зустрічаються: {first_fighter.name} та {second_fiter.name}! \nПобажаємо їм успіху! До бою!\n')
        sleep(4)
        first_fighter.battle(second_fiter)
        if first_fighter.health <= 0:
            winner = second_fiter
            looser = first_fighter
            challengers.remove(first_fighter)
        else:
            winner = first_fighter
            looser = second_fiter
            challengers.remove(second_fiter)
        sleep(3)
        print(f'Вітаємо переможця поєдинку, це {winner.name}! Він іде відновлювати сили під ваші оплески.')
        if len(challengers) == 1:
            print(f'{looser.name} нажаль вибуває, це кінець.')
        else:
            print(f'{looser.name} нажаль вибуває, приберіть арену для наступного поєдинку.')
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
    Hello.bye()
