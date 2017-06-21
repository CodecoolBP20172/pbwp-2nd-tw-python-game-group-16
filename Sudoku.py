import random
import os
import string
player_input = 8
row = 0
column = "q"
mapx = 1
end_game = 1
x = "x"
add_ = 10
play_area = 0
source_list = 0
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


def generator():
    for i in range(random.randint(1, 7)):
        print("")
        add_ = random.randint(0, 8)
        del play_area[add_]
        play_area.insert(add_, source_list[add_])


def change():
    global player_input
    global row
    global column
    global end_game
    list_index = 0
    try:
        while not end_game == 3:
            player_input = int(input("Please enter a number: "))
            row = input("Row (Letter): ")
            column = int(input("Column (Number): "))
            column = column - 1
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
                    print("You can't modify that")
            x_map()
    except ValueError:
        print("Have you finished the game? ")
        end_game = input("1: No, 2: Yes ")


if mapx == 1:
    for item in range(len(x_list)):
        play_area = x_list[item]
        source_list = complete_list[item]
        generator()
        replace_null()
        os.system('clear')
        x_map()

while not end_game == 3:
    change()
    if x_list == complete_list:
        print("Congratulations! You solved it!")
        end_game = 3
    else:
        os.system('clear')
        replace_null()
        x_map()
        print("Are you sure about that?")
        end_game = 1
