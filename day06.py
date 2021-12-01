with open('input.txt', 'r') as f:
    arr = [int(e) for e in f.read().split()]

prev = []
count = 0
while True:
    count += 1
    prev.append(arr.copy())

    i = arr.index(max(arr))
    n = arr[i]
    arr[i] = 0

    for x in range(n):
        arr[(i + 1 + x) % len(arr)] += 1

    if arr in prev:
        prev_app = prev.index(arr)
        break;

print(count - prev_app)
print(count)

    
