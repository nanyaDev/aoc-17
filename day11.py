with open('input.txt', 'r') as f:
    data = f.read().strip().split(',')

q = 0
r = 0
s = 0

tracker = []
for mv in data:
    if mv == 'n':
        q += 1
        r -= 1
    if mv == 'ne':
        q += 1
        s -= 1
    if mv == 'se':
        r += 1
        s -= 1
    if mv == 's':
        r += 1
        q -= 1
    if mv == 'sw':
        s += 1
        q -= 1
    if mv == 'nw':
        s += 1
        r -= 1

    manhattan = (abs(q) + abs(r) + abs(s)) // 2
    tracker.append(manhattan)

print(max(tracker))


