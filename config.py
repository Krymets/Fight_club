from hero_classes_pack.class_knight import Knight
from hero_classes_pack.class_mage import Mage
from hero_classes_pack.hero_classes import Hero

knight = Knight('Лицар Річард "Гострий меч"', 50, 25, 20, 'меч')  # name, health, armor, power, weapon
rascal = Hero('Пройдисвіт Петро "Підступний ніж"', 95, 5, 7, 'ніж')
hunter = Hero('Мисливець Хантер "Довгий лук"', 70, 10, 15, 'лук')
assassin = Hero('Вбивця Эціо "Друг Леонардо Да Вінчі"', 70, 3, 20, 'метальні ножі')
mage = Mage('Маг Гендальф "Білий"', 85, 0, 16, 'посох')

challengers = [knight, rascal, hunter, assassin, mage]

