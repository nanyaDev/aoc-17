with open('input.txt', 'r') as f:
    inp = [int(e) for e in f.readlines()]

i = 0
count = 0

while True:
    prev = i
    i += inp[i]
    count += 1

    if i < 0 or i >= len(inp):
        break;

    if inp[prev] >= 3:
        inp[prev] -= 1
    else: 
        inp[prev] += 1

print(count)
