with open('input.txt', 'r') as f:
    arrs = [list(map(int, arr.split())) for arr in f.readlines()]

ret1 = 0
ret2 = 0

for arr in arrs:
    ret1 += max(arr) - min(arr)

    for i in range(len(arr)):
        for j in range(len(arr)):
            x = arr[i]
            y = arr[j]
            if i != j and x >= y and x % y == 0:
                ret2 += x // y

print(ret1)
print(ret2)
