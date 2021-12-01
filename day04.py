from collections import Counter

with open('input.txt', 'r') as f:
    lines = f.readlines()
    data = [line.split() for line in lines]

def isValid(line):
    for i in range(len(line)):
        for j in range(i + 1, len(line)):
            if line[i] == line[j]:
                return False
    return True;


ret1 = 0
for line in data:
    if isValid(line):
        ret1 += 1
    
print(ret1)

ret2 = 0
for line in data:
    if isValid([Counter(word) for word in line]):
        ret2 += 1
    
print(ret2)
        
