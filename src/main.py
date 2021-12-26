def dead_state(width, height):
    board = []
    for _ in range(height):
        temp = []
        for _ in range(width):
            temp.append(0)
        board.append(temp)
    return board

