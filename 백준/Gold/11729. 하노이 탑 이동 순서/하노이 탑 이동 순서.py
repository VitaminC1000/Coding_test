def moveHanoi(disk, start, target, auxiliary, moves):

    if disk == 1:
        moves.append((start, target))
        return
    
    moveHanoi(disk - 1, start, auxiliary, target, moves)

    moves.append((start, target))

    moveHanoi(disk - 1, auxiliary, target, start, moves)

n = int(input())
moves = [] 
moveHanoi(n, 1, 3, 2, moves)

print(len(moves))
for move in moves:
    print(move[0], move[1])