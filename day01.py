with open('input.txt', 'r') as f:
    inp = [int(e) for e in list(f.read().strip())]

ret = 0

for i in range(len(inp)):
    if inp[i] == inp[i - len(inp) // 2]:
        ret += inp[i]

print(ret)
