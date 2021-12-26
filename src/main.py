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

