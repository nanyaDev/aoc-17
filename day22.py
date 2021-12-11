with open('input.txt', 'r') as f:
    data = [list(line) for line in f.read().strip().split('\n')]

infected = set()
weakened = set()
flagged = set()

for i in range(len(data)):
    for j in range(len(data[0])):
        if data[i][j] == '#':
            infected.add((i,j)) 

i = len(data) // 2
j = len(data[0]) // 2
curr = (i, j)

directions = [(-1,0), (0,1), (1,0), (0,-1)]
d = 0

count = 0
for n in range(10_000_000):
    if curr in weakened:
        weakened.remove(curr)
        infected.add(curr)
        count += 1
    elif curr in infected:
        infected.remove(curr)
        flagged.add(curr)
        d = (d + 1) % len(directions)
    elif curr in flagged:
        flagged.remove(curr)
        d = (d + 2) % len(directions)
    else:
        weakened.add(curr)
        d = (d - 1) % len(directions)

    i, j = curr
    di, dj = directions[d]

    curr = (i + di, j + dj)

print(count)

