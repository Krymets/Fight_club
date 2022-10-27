from hero_classes_pack.class_assassin import Assassin
from hero_classes_pack.class_hunter import Hunter
from hero_classes_pack.class_knight import Knight
from hero_classes_pack.class_mage import Mage
from hero_classes_pack.class_rascal import Rascal

knight = Knight('Лицар Річард "Гострий меч"', 50, 25, 16, 'меч')  # name, health, armor, power, weapon
rascal = Rascal('Пройдисвіт Петро "Підступний ніж"', 95, 5, 11, 'ніж')
hunter = Hunter('Мисливець Хантер "Довгий лук"', 70, 10, 15, 'лук')
assassin = Assassin('Вбивця Эціо "Друг Леонардо Да Вінчі"', 65, 3, 16, 'метальні ножі')
mage = Mage('Маг Гендальф "Білий"', 80, 0, 13, 'посох')

challengers = [knight, rascal, hunter, assassin, mage]
