import random
import time

# This size looks nice in my neovim terminal popup
# Change it to your liking
WIDTH = 30
HEIGHT = 14

def dead_state(width, height):
    board = []
    for _ in range(height):
        temp = []
        for _ in range(width):
            temp.append(0)
        board.append(temp)
    return board

def random_state(width, height):
    state = dead_state(width, height)
    for h in range(height):
        for w in range(width):
            state[h][w] = random.choice((0, 1))
    return state

def create_board(state):
    starter = ""
    for _ in range(len(state[0]) + 2):
        starter += "-"
    print(starter)
    for i in range(len(state)):
        print("|", end="")
        for j in range(len(state[0])):
            print("#" if state[i][j] else " ", end="")
        print("|")
    print(starter)

def next_board_state(state):
    new_state = []
    for h in range(len(state)):
        temp = []
        for w in range(len(state[0])):
            neighbors = 0
            cell = state[h][w]
            top = state[h-1][w]
            topleft = state[h-1][w-1]
            left = state[h][w-1]
            right = state[h][w+1] if w != len(state[0])-1 else 0
            bottom = state[h+1][w] if h != len(state)-1 else 0
            bottomleft = state[h+1][w-1] if h != len(state)-1 else 0
            topright = state[h-1][w+1] if w != len(state[0])-1 else 0
            bottomright = state[h+1][w+1] if h!= len(state)-1 and w != len(state[0])-1 else 0
            # calc neighbors
            if h == 0 and w == 0:
                neighbors = bottom + right + bottomright
            elif h == 0 and w == len(state[0])-1:
                neighbors = bottom + left + bottomleft
            elif h == len(state)-1 and w == 0:
                neighbors = top + right + topright
            elif h == len(state)-1 and w == len(state[0])-1:
                neighbors = top + left + topleft
            elif h == 0:
                neighbors = bottom + right + left + bottomleft + bottomright 
            elif w == 0:
                neighbors = top + bottom + right + topright + bottomright
            elif h == len(state)-1:
                neighbors = top + left + right + topleft + topright
            elif w == len(state[0])-1:
                neighbors = top + bottom + left + topleft + bottomleft
            else:
                neighbors = top + bottom + right + left + topright + topleft + bottomright + bottomleft
            # decide if living or not
            if cell:
                if neighbors < 2:
                    cell = 0
                elif neighbors == 3 or neighbors == 2:
                    cell = 1
                elif neighbors > 3:
                    cell = 0
            else:
                if neighbors == 3:
                    cell = 1
            temp.append(cell)
        new_state.append(temp)
    return(new_state)

state = random_state(WIDTH, HEIGHT)
create_board(state)
while state != dead_state(WIDTH, HEIGHT) and state != next_board_state(state):
    time.sleep(0.5)
    state = next_board_state(state)
    create_board(state)
