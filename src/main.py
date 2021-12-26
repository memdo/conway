import random

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

