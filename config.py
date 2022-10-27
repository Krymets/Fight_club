from hero_classes_pack.class_assassin import Assassin
from hero_classes_pack.class_hunter import Hunter
from hero_classes_pack.class_knight import Knight
from hero_classes_pack.class_mage import Mage
from hero_classes_pack.class_rascal import Rascal

knight_stats = 50, 25, 16
rascal_stats = 50, 25, 16
hunter_stats = 50, 25, 16
assassin_stats = 50, 25, 16
mage_stats = 50, 25, 16

knight = Knight('Лицар Річард "Гострий меч"', knight_stats[0], knight_stats[1], knight_stats[2], 'меч')
rascal = Rascal('Пройдисвіт Петро "Підступний ніж"', rascal_stats[0], rascal_stats[1], rascal_stats[2], 'ніж')
hunter = Hunter('Мисливець Хантер "Довгий лук"', hunter_stats[0], hunter_stats[1], hunter_stats[2], 'лук')
assassin = Assassin('Вбивця Эціо "Друг Леонардо Да Вінчі"', assassin_stats[0], assassin_stats[1], assassin_stats[2], 'метальні ножі')
mage = Mage('Маг Гендальф "Білий"', mage_stats[0], mage_stats[1], mage_stats[2], 'посох')

challengers = [knight, rascal, hunter, assassin, mage]
