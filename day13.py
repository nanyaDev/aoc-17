with open('input.txt', 'r') as f:
    data = f.readlines()

scanners = {}
for line in data:
    d, r = line.split(': ')
    d = int(d)
    r = int(r)

    scanners[d] = r

severity = 0
for i in range(max(scanners.keys()) + 1):
    if i not in scanners:
        continue

    if i % (2 * scanners[i] - 2) == 0:
        severity += i * scanners[i]

print('Part 1:', severity)

delay = 0
while True:
    caught = False
    for i in range(max(scanners.keys()) + 1):
        if i not in scanners:
            continue

        if (delay + i) % (2 * scanners[i] - 2) == 0:
            caught = True
            break

    if not caught:
        print('Part 2:', delay)
        break

    delay += 1

