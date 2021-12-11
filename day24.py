from itertools import chain

with open('input.txt', 'r') as f:
    data = f.read().splitlines()

for i in range(len(data)):
    x, y = data[i].split('/')
    data[i] = (int(x), int(y))

bridges = set()
bridges.add(((0,0),))

l = 1
while True:
    prev = bridges.copy()
    for bridge in prev:
        if len(bridge) < l:
            continue

        if len(bridge) == 1:
            req = 0
        else:
            p1, p2 = bridge[-1]
            req = p2 if p1 == bridge[-2][0] or p1 == bridge[-2][1] else p1

        for connector in data:
            plug, port = connector

            if connector in bridge:
                continue

            if plug == req or port == req:
                new = bridge + ((plug, port),)
                bridges.add(new)

    if len(bridges) == len(prev):
        break

    l += 1

ret1 = 0
ret2 = 0

for bridge in bridges:
    s = sum(chain(*bridge))

    if s > ret1:
        ret1 = s

    if s > ret2 and len(bridge) == l:
       ret2 = s 

print(ret1)
print(ret2)

