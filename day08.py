from collections import defaultdict

with open('input.txt', 'r') as f:
    data = f.readlines()

# parse
running_max = 0
registers = defaultdict(int)

for line in data:
    counter, change, n, _, x, op, y = line.split()

    condition = f'registers["{x}"] {op} {y}'

    if eval(condition):
        if change == 'inc':
            registers[counter] += int(n)
        else:
            registers[counter] -= int(n)

    curr_max = max(registers.values()) 
    if (curr_max > running_max):
        running_max = curr_max

print(max(registers.values()))
print(running_max)








