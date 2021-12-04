with open('input.txt', 'r') as f:
    data = f.read().strip().split(',')
    data = [int(n) for n in data]

data = ','.join([str(i) for i in data])
new = []

for n in data:
    new.append(ord(n))

new += [17, 31, 73, 47, 23]
data = new

def reverseArr(arr, s, l):
    arr = arr[s:] + arr[:s]
    arr = arr[:l][::-1] + arr[l:]
    arr = arr[len(arr) - s:] + arr[:len(arr) - s]

    return arr

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

print(ret)

    
