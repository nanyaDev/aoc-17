import re
from copy import deepcopy
from collections import defaultdict

with open('input.txt', 'r') as f:
    data = f.read().strip().split('\n')

for i, line in enumerate(data):
    vectors = []
    for vector in re.findall(r'<([^<>]+)>', line):
        vectors.append([int(n) for n in vector.split(',')])

    data[i] = vectors

mags = []
for i, vectors in enumerate(data):
    p, v, a = vectors

    mag = sum([n ** 2 for n in a])
    mags.append(mag)

ans = mags.index(min(mags))
print('Part 1:', ans)

curr = deepcopy(data)
counts = []
while True:
    counts.append(len(curr))

    last100 = counts[-100:]
    if len(counts) > 100 and last100.count(last100[0]) == len(last100):
        break

    for i, vectors in enumerate(curr):
        p, v, a = vectors

        v = [sum(t) for t in zip(v,a)]
        p = [sum(t) for t in zip(p,v)]

        curr[i] = [p,v,a]

    positions = defaultdict(int)
    for vectors in curr:
        pos = tuple(vectors[0])
        positions[pos] += 1

    new = []
    for i, vectors in enumerate(curr):
        pos = tuple(vectors[0])
        if positions[pos] == 1:
            new.append(vectors)

    curr = new

print('Part 2:', len(curr))

