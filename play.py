from Person import *

def menu(player):
    while True:
        print("1) Сражаться")
        print("2) Посмотреть статистику")
        print("3) Выход")
        # try и except просто фиксят ошибки. Не обращайте внимания.
        try:
            n = int(input("Введите число: "))

            if n == 1:
                menu_fight(player)
            elif n == 2:
                menu_stats(player)
            elif n == 3:
                exit() 
            else:
                print("Чего ждем?")

        except NameError:
            print("Введите число")
        except SyntaxError:
            print("Введите число")


def menu_fight(player):
    pass

def menu_stats(player):
    player.display_info()
    