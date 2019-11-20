# Problem 3: SOLVED

f = open('DATA31.txt', 'r')
for w in range(10):
    raw = f.readline().split(" ")
    jump_height = int(raw[0])
    width = int(raw[1])
    height = int(raw[2].replace('\n', ''))
    board = []
    for q in range(height): 
        board.append(f.readline().replace('\n', ''))
    
    # Find Position of LOO E.G
    pos = [board[height-2].index('L'), height-2]
    goal = [board[height-2].index('G'), height-2]

    # Create the Jump Function
    def jump():
        y = pos[1]
        x = pos[0]
        # Go Up
        for i in range(1, jump_height+1):
            dy = y-i
            if dy <= -1: return False
            if board[dy][x] == '@':
                return False
            if board[dy][x+1] != '@' and board[dy][x+2] != '@':
                current_row = [board[y-p][x+2] for p in range(0, i+1)]
                if '@' in current_row: return False
                return True
        return False

    # Progress
    while True:
        x = pos[0]
        y = pos[1]
        if pos == goal:
            flag = True
            break
        # Check Forward
        if board[y][x+1] != '@':
            pos[0] += 1
            continue
        else:
            if jump():
                pos[0] += 2
            else:
                pos[0] += 2
                flag = False
                break
    
    # Final Statement
    if flag:
        print('CLEAR')
    else:
        print(pos[0])

f.close()