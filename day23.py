from collections import defaultdict

with open('input.txt', 'r') as f:
    data = f.read().strip().split('\n')

reg = defaultdict(int)

def getVal(z):
    if 'a' <= z <= 'z':
        return reg[z]
    else:
        return int(z)
flag = False

count = 0
i = 0
while 0 <= i < len(data):
    cmd, x, y = data[i].split(' ')

    if cmd == 'set':
        reg[x] = getVal(y)
    if cmd == 'sub':
        reg[x] -= getVal(y)
    if cmd == 'mul':
        reg[x] *= getVal(y)
        count += 1
    if cmd == 'jnz':
        if getVal(x) != 0:
            i += getVal(y)
            continue

    i += 1

print('Part 1:', count)

def isPrime(n):
    return n > 1 and all(n % i for i in range(2, int(n ** 0.5) + 1))

ret = 0
for b in range(109300, 126301, 17):
  if not isPrime(b):
    ret += 1

print('Part 2:', ret)



