import random
import os
import string
mapx = 1
end_game = 1
x = "x"
random_number = 1
end = 0

x_list = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0]]

complete_list = [[5, 3, 4, 6, 7, 8, 9, 1, 2],
                 [6, 7, 2, 1, 9, 5, 3, 4, 8],
                 [1, 9, 8, 3, 4, 2, 5, 6, 7],
                 [8, 5, 9, 7, 6, 1, 4, 2, 3],
                 [4, 2, 6, 8, 5, 3, 7, 9, 1],
                 [7, 1, 3, 9, 2, 4, 8, 5, 6],
                 [9, 6, 1, 5, 3, 7, 2, 8, 4],
                 [2, 8, 7, 4, 1, 9, 6, 3, 5],
                 [3, 4, 5, 2, 8, 6, 1, 7, 9]]

abc_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']


def replace_null():
    for item in range(9):
        for iteration in range(9):
            if x_list[item][iteration] == 0:
                x_list[item][iteration] = ""


def x_map():
    print("   1  2  3  4  5  6  7  8  9")
    for item in range(len(x_list)):
        if item == 2 or item == 5:
            print(abc_list[item], ('[{:>1}  {:>1}  {:>1}][{:>1}  {:>1}  {:>1}][{:>1}  {:>1}  {:>1}]'
                                   .format(x_list[item][0], x_list[item][1], x_list[item][2], x_list[item][3],
                                           x_list[item][4], x_list[item][5], x_list[item][6], x_list[item][7],
                                           x_list[item][8])), '\n')
        else:
            print(abc_list[item], ('[{:>1}  {:>1}  {:>1}][{:>1}  {:>1}  {:>1}][{:>1}  {:>1}  {:>1}]'
                                   .format(x_list[item][0], x_list[item][1], x_list[item][2], x_list[item][3],
                                           x_list[item][4], x_list[item][5], x_list[item][6], x_list[item][7],
                                           x_list[item][8])))


def generator(diff):
    if diff == 1:
        for i in range(7):
            print("")
            add_ = random.randint(0, 8)
            del play_area[add_]
            play_area.insert(add_, source_list[add_])
    elif diff == 2:
        for i in range(4):
            print("")
            add_ = random.randint(0, 8)
            del play_area[add_]
            play_area.insert(add_, source_list[add_])
    elif diff == 3:
        for i in range(2):
            print("")
            add_ = random.randint(0, 8)
            del play_area[add_]
            play_area.insert(add_, source_list[add_])
    elif diff == 666:
        for i in range(9):
            print("")
            del play_area[i]
            play_area.insert(i, source_list[i])


def change():
    global end_game
    list_index = 0
    try:
        while not end_game == 3:
            player_input = int(input("Please enter a number or a letter if you think you are done: "))
            row = input("Row (Letter): ")
            try: 
                column = int(input("Column (Number): "))
                column = column - 1
            except ValueError:
                os.system('clear')
                print("Not valid column!")
                x_map()
                continue

            if column < 1 or column > 9:
                os.system('clear')
                print("Not a valid number!")
                x_map()
                continue
            os.system('clear')
            if row in abc_list:
                list_index = abc_list.index(row)
                if x_list[list_index][column] == "":
                    del x_list[list_index][column]
                    x_list[list_index].insert(column, player_input)
                elif x_list[list_index][column] != "" and x_list[list_index][column] != complete_list[list_index][column]:
                    del x_list[list_index][column]
                    x_list[list_index].insert(column, player_input)
                else:
                    print('\x1b[0;30;41m' + "You can't modify that" + '\x1b[0m')
            x_map()
    except ValueError:
        print("Have you finished the game? ")
        end_game = int(input("1: No, 2: Yes "))


if mapx == 1:
    print(
          "   .d8888b.               888          888               888", "\n"
          "  d88P  Y88b              888          888               888", "\n"
          "  Y88b.                   888          888               888", "\n"
          "   Y888b.   888  888  .d88888  .d88b.  888  888 888  888 888 ", "\n"
          "      Y88b. 888  888 d88  888 d88  88b 888 .88P 888  888 888 ", "\n"
          "        888 888  888 888  888 888  888 888888K  888  888 Y8P ", "\n"
          " Y88b  d88P Y88b 888 Y88b 888 Y88..88P 888  88b Y88b 888    ", "\n"
          "   Y8888P     Y88888   Y88888   Y88P   888  888   Y88888 888 ", "\n")
    print("Please select a difficulty level!", "\n", "1: Easy,", "\n", "2: Medium", "\n", "3: Hardcore")
    diff = int(input())
    if diff == 666:
        for item in range(len(x_list)):
            play_area = x_list[item]
            source_list = complete_list[item]
            generator(diff)
            replace_null()
            os.system('clear')
            x_map()
    else:
        while diff == 0 or diff > 3:
            os.system('clear')
            print("That isn't a valid level!", "\n", "1: Easy,", "\n", "2: Medium", "\n", "3: Hardcore")
            diff = int(input())
        for item in range(len(x_list)):
            play_area = x_list[item]
            source_list = complete_list[item]
            generator(diff)
            replace_null()
            os.system('clear')
            x_map()

while not end_game == 3:
    change()
    if x_list == complete_list and end_game == 2:
        os.system('clear')
        print("  __   __  _______  __   __    _     _  _______  __    _  __  ", '\n',
              "|  | |  ||       ||  | |  |  | | _ | ||       ||  |  | ||  | ", '\n',
              "|  |_|  ||   _   ||  | |  |  | || || ||   _   ||   |_| ||  | ", '\n',
              "|       ||  | |  ||  |_|  |  |       ||  | |  ||       ||  | ", '\n',
              "|_     _||  |_|  ||       |  |       ||  |_|  ||  _    ||__| ", '\n',
              "  |   |  |       ||       |  |   _   ||       || | |   | __  ", '\n',
              "  |___|  |_______||_______|  |__| |__||_______||_|  |__||__| ")
        end_game = 3
    else:
        os.system('clear')
        replace_null()
        x_map()
        print("Are you sure about that?")
        end_game = 1
