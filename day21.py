from math import sqrt

with open('input.txt', 'r') as f:
    data = f.read().strip().split('\n')

image = ['.#.','..#','###']

for n, rule in enumerate(data):
    i, o = rule.split(' => ')

    i = i.split('/')
    o = o.split('/')

    data[n] = [i,o]

def breakdownImage(image):
    s = len(image)
    ret = []

    l = 2 if s % 2 == 0 else 3
    
    subs = []
    for i in range(0, s, l):
        for j in range(0, s, l):
            sub = []
            for di in range(l):
                row = ''
                for dj in range(l):
                    val = image[i + di][j + dj]
                    row += val

                sub.append(row)
            subs.append(sub)

    return subs

def rejoinImage(subs):
    si = int(sqrt(len(subs))) 
    sl = len(subs[0][0])
    il = sl * si

    image = []
    for i in range(il):
        row = ''
        start = i // sl * si
        end = start + si
        for n in range(start, end):
            ii = i % sl
            row += subs[n][ii]

        image.append(row)

    return image

def rotate(image):
    return [''.join(t) for t in zip(*image[::-1])]

def flip(image):
    return [row[::-1] for row in image]

def patternMatch(i1):
    i2 = flip(i1)

    for i, o in data:
        for _ in range(4):
            if i1 == i or i2 == i:
                return o
            
            i1 = rotate(i1)
            i2 = rotate(i2)

    return i1

for i in range(18):
    print('Iteration', i)
    subs = breakdownImage(image)
    
    for n in range(len(subs)):
        subs[n] = patternMatch(subs[n])
    
    image = rejoinImage(subs)

ans = ''.join(image).count('#')
print('Result:', ans)

