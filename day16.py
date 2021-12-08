with open('input.txt', 'r') as f:
    data = f.read().strip().split(',')

commands = []
for line in data:
    cmd = line[0]

    if cmd == 's':
        x = int(line[1:])
        commands.append([cmd, x])
    if cmd == 'x':
        x, y = [int(n) for n in line[1:].split('/')]
        commands.append([cmd, x, y])
    if cmd == 'p':
        x, y = line[1:].split('/')
        commands.append([cmd, x, y])

def dance(p):
    for command in commands:
        cmd, *args = command
        if cmd == 's':
            x, = args
            p = p[-x:] + p[:-x]
        if cmd == 'x':
            x, y = args
            p[x], p[y] = p[y], p[x]
        if cmd == 'p':
            x, y = args
            xx = p.index(x)
            yy = p.index(y)
            p[xx], p[yy] = p[yy], p[xx]

    return p

ans = dance(list('abcdefghijklmnop'))
print('Part 1:', ''.join(ans))



initial = list('abcdefghijklmnop')
curr = initial.copy()

# exit()
i = 0
while i < 1_000_000_000:
    if curr == initial and i > 0:
        i *= 1_000_000_000 // i

    curr = dance(curr) 
    i += 1

print('Part 2:' ,''.join(curr))

