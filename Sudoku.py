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

ax = [0, 0, 0, 0, 0, 0, 0, 0, 0]
bx = [0, 0, 0, 0, 0, 0, 0, 0, 0]
cx = [0, 0, 0, 0, 0, 0, 0, 0, 0]
dx = [0, 0, 0, 0, 0, 0, 0, 0, 0]
ex = [0, 0, 0, 0, 0, 0, 0, 0, 0]
fx = [0, 0, 0, 0, 0, 0, 0, 0, 0]
gx = [0, 0, 0, 0, 0, 0, 0, 0, 0]
hx = [0, 0, 0, 0, 0, 0, 0, 0, 0]
ix = [0, 0, 0, 0, 0, 0, 0, 0, 0]

x_list = [ax, bx, cx, dx, ex, fx, gx, hx, ix]

a1 = [5, 3, 4, 6, 7, 8, 9, 1, 2]
b1 = [6, 7, 2, 1, 9, 5, 3, 4, 8]
c1 = [1, 9, 8, 3, 4, 2, 5, 6, 7]
d1 = [8, 5, 9, 7, 6, 1, 4, 2, 3]
e1 = [4, 2, 6, 8, 5, 3, 7, 9, 1]
f1 = [7, 1, 3, 9, 2, 4, 8, 5, 6]
g1 = [9, 6, 1, 5, 3, 7, 2, 8, 4]
h1 = [2, 8, 7, 4, 1, 9, 6, 3, 5]
i1 = [3, 4, 5, 2, 8, 6, 1, 7, 9]


def replace_null():
    for item in range(9): 
        for iteration in range(9): 
            if x_list[item][iteration] == 0:
                x_list[item][iteration] = ""


def x_map():
    print("     1  2  3   4  5  6   7  8  9")
    print("  a",('{:>1}  {:>1}  {:>1}'.format(ax[0], ax[1], ax[2])))#, ax[3:6], ax[6:9]), '\n', ' b', bx[0:3], bx[3:6], bx[6:9], '\n', ' c',
          # cx[0:3], cx[3:6], cx[6:9], '\n')
    print("  d", dx[0:3], dx[3:6], dx[6:9], '\n', ' e', ex[0:3], ex[3:6], ex[6:9], '\n', ' f',
          fx[0:3], fx[3:6], fx[6:9], '\n')
    print("  g", gx[0:3], gx[3:6], gx[6:9], '\n', ' h', hx[0:3], hx[3:6], hx[6:9], '\n', ' i',
          ix[0:3], ix[3:6], ix[6:9], '\n')


def generator():
    for i in range(random.randint(1, 7)):
        add_ = random.randint(0, 8)
        del play_area[add_]
        play_area.insert(add_, source_list[add_])


def change():
    global player_input
    global row
    global column
    global end_game
    try:
        while not end_game == 3:
            player_input = int(input("Please enter a number: "))
            row = input("Row (Letter): ")
            column = int(input("Column (Number): "))
            column = column - 1
            if row == "a":
                del ax[column]
                ax.insert(column, player_input)
            elif row == "b":
                del bx[column]
                bx.insert(column, player_input)
            elif row == "c":
                del cx[column]
                cx.insert(column, player_input)
            elif row == "d":
                del dx[column]
                dx.insert(column, player_input)
            elif row == "e":
                del ex[column]
                ex.insert(column, player_input)
            elif row == "f":
                del fx[column]
                fx.insert(column, player_input)
            elif row == "g":
                del gx[column]
                gx.insert(column, player_input)
            elif row == "h":
                del hx[column]
                hx.insert(column, player_input)
            elif row == "i":
                del ix[column]
                ix.insert(column, player_input)
            os.system('clear')
            x_map()
            # print(row, column, player_input)
    except ValueError:
        print("Have you finished the game? ")
        end_game = input("1: No, 2: Yes ")


if mapx == 1:
    play_area = ax
    source_list = a1
    generator()
    play_area = bx
    source_list = b1
    generator()
    play_area = cx
    source_list = c1
    generator()
    play_area = dx
    source_list = d1
    generator()
    play_area = ex
    source_list = e1
    generator()
    play_area = fx
    source_list = f1
    generator()
    play_area = gx
    source_list = g1
    generator()
    play_area = hx
    source_list = h1
    generator()
    play_area = ix
    source_list = i1
    generator()
    replace_null()
    x_map()

while not end_game == 3:
    change()

    if ax == a1:
        end = end + 1
    elif bx == b1:
        end = end + 1
    elif cx == c1:
        end = end + 1
    elif dx == d1:
        end = end + 1
    elif ex == e1:
        end = end + 1
    elif fx == f1:
        end = end + 1
    elif gx == g1:
        end = end + 1
    elif hx == h1:
        end = end + 1
    elif ix == i1:
        end = end + 1
    elif end == 9:
        print("Congratulations! You solved it!")
        end_game = 3
    else:
        os.system('clear')
        replace_null()
        x_map()
        print("Are you sure about that?")
        end_game = 1
