with open('input.txt', 'r') as f:
    data = f.read()

garbage = False
score = 0
nest = 0
garbage_count = 0

i = 0
while i < (len(data)):
    char = data[i]

    if char == '!':
        i += 2
        continue 

    if char == '<' and garbage == False:
        garbage = True
        garbage_count -= 1

    if char == '>' and garbage == True:
        garbage = False

    if garbage == False and char == '{':
        nest += 1

    if garbage == False and char == '}':
        score += nest
        nest -= 1

    if garbage:
        garbage_count += 1

    i += 1

print(score)
print(garbage_count)


