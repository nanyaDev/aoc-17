with open('input.txt', 'r') as f:
    maze = [list(line) for line in f.read().split('\n')]

i = 0
j = 0

d = 'down'

for coord in range(len(maze[0])):
    if maze[0][coord] != ' ':
        j = coord

pattern = ''
count = 0
while True:
    count += 1
    if d == 'up': i -= 1
    if d == 'down': i += 1
    if d == 'left': j -= 1
    if d == 'right': j += 1

    if 'A' <= maze[i][j] <= 'Z':
        pattern += maze[i][j]

    if maze[i][j] == '+':
        if d == 'up' or d == 'down':
            d = 'right' if maze[i][j + 1] != ' ' else 'left'
        elif d == 'left' or d == 'right':
            d = 'up' if maze[i - 1][j] != ' ' else 'down'

    if maze[i][j] == ' ':
        break

print('Part 1:', pattern)
print('Part 2:', count)

