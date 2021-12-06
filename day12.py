with open('input.txt', 'r') as f:
    data = f.readlines()

connections = {}
houses = set()
for line in data:
    p, c = line.split(' <-> ')

    p = int(p)
    c = [int(n) for n in c.split(',')]

    connections[p] = c
    houses.update(c)

def getGroup(house):
    houses = { house }

    while True:
        prev = houses.copy()

        for house in prev:
            houses.update(connections[house])

        if (len(prev) == len(houses)):
            return houses

print('Part 1:', len(getGroup(0)))

connected = set()
count = 0
for house in houses:
    if house in connected:
        continue

    connected.update(getGroup(house))
    count += 1

print('Part 2:', count)
