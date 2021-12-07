def reverseArr(arr, s, l):
    arr = arr[s:] + arr[:s]
    arr = arr[:l][::-1] + arr[l:]
    arr = arr[len(arr) - s:] + arr[:len(arr) - s]

    return arr

def knotHash(s):
    data = []
    for ch in s:
        data.append(ord(ch))

    data += [17, 31, 73, 47, 23]

    arr = list(range(256))
    skip = 0
    curr = 0

    for x in range(64):
        for l in data:
            arr = reverseArr(arr, curr, l)
            curr += l + skip
            curr %= len(arr)
            skip += 1

    dense = []
    for x in range(16):
        curr = 0
        for y in range(16):
            curr ^= arr[x*16 + y]

        dense.append(curr)


    ret = ''
    for n in dense:
        hexa = hex(n)[2:]

        if len(hexa) == 1:
            hexa = '0' + hexa

        ret += hexa

    return ret

from collections import Counter, deque
from itertools import product

input = 'hfdlxzhv'

rows = []
for i in range(128):
    s = input + '-' + str(i)

    hexa = knotHash(s)

    binary = ''
    for ch in hexa:
        binary += bin(int(ch, 16))[2:].zfill(4)

    rows.append(binary)

print('Part 1:', Counter(''.join(rows))['1'])

acc = []
groups = 0
for i in range(128):
    for j in range(128):
        if rows[i][j] == '0' or (i, j) in acc:
            continue

        acc.append((i,j))
        q = deque([(i,j)])
        groups += 1

        while q:
            x, y = q.popleft()

            for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                ii = x + dx
                jj = y + dy
                if ii < 0 or ii >= 128 or jj < 0 or jj >= 128:
                    continue
                if rows[ii][jj] == '0' or (ii, jj) in acc:
                    continue
                else:
                    acc.append((ii, jj))
                    q.append((ii, jj))

print('Part 2:', groups)
