from time import sleep
from config import *


class Hello:
    @staticmethod
    def hello():
        print('Вітаємо сьогоднішніх претендентів кубку короля\n')
        sleep(5)
        print(knight.__str__())
        sleep(5)
        print(rascal.__str__())
        sleep(5)
        print(assassin.__str__())
        sleep(5)
        print(hunter.__str__())
        sleep(5)
        print(mage.__str__())
        sleep(5)

    @staticmethod
    def bye():
        print('Добре, можемо і перенести, нічого страшного. Розходьтесь...')

    @staticmethod
    def yes_no():
        return input('Наступає час початку битви і король має дати команду починати битву (так / ні) >>> ').lower()
