from itertools import product

input = 289326

ring = 1
i = 0

while True:
    n = (2 * i + 1) ** 2

    if n >= input:
        ring = i
        break;
    else:
        i += 1

horiz = ring
vert = ring - 1

jumps = input - (2 * i - 1) ** 2 - 1

edge = 2 * i

for i in range(jumps):
    side = (i + 1) // edge

    if (side == 0): vert -= 1
    if (side == 1): horiz -= 1
    if (side == 2): vert += 1
    if (side == 3): horiz += 1

ans = abs(horiz) + abs(vert)

print(ans)

def part2():
    dict = { (0,0): 1 }

    n = 1
    x = 1
    y = 0

    while True:
        nodes = (2 * n) * 4

        for i in range(nodes):
            offsets = product([-1,0,1], repeat=2)
            coords = [(x + a, y + b) for a, b in offsets]

            val = sum([dict.get(coord, 0) for coord in coords])

            if val > input:
                return val
            else:
                dict[(x,y)] = val

                side = (i + 1) // (2 * n)

                if (side == 0): y -= 1
                if (side == 1): x -= 1
                if (side == 2): y += 1
                if (side == 3): x += 1

        x += 1
        n += 1

print(part2())

