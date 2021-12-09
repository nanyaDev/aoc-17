from collections import defaultdict

with open('input.txt', 'r') as f:
    data = f.read().strip().split('\n')

def run(n, reg, rcvQ):
    sendQ = []

    while True:
        line = data[n]

        cmd = line.split()[0]
        x = line.split()[1]
        if cmd == 'snd' or cmd == 'jgz':
            x = reg[x] if 'a' <= x <= 'z' else int(x)

        if len(line.split()) > 2:
            y = line.split()[2]
            y = reg[y] if 'a' <= y <= 'z' else int(y)

        if cmd == 'snd':
            sendQ.append(x)
        if cmd == 'set':
            reg[x] = y
        if cmd == 'add':
            reg[x] += y
        if cmd == 'mul':
            reg[x] *= y
        if cmd == 'mod':
            reg[x] %= y
        if cmd == 'rcv':
            if not rcvQ:
                return n, sendQ 

            reg[x] = rcvQ.pop(0)
        if cmd == 'jgz':
            if x > 0:
                n += y
                continue

        n += 1

regi = defaultdict(int)
regj = defaultdict(int)

regi['p'] = 0
regj['p'] = 1

qi = []
qj = []

i = 0
j = 0

ret = 0
while True:
    i, qj = run(i, regi, qi)

    if not qi and not qj:
        break;

    j, qi = run(j, regj, qj)
    ret += len(qi)

    if not qi and not qj:
        break;

print(ret)
 
