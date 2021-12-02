import re

with open('input.txt', 'r') as f:
    data = f.readlines()

towers = []
subtowers = []
towers_to_subs = {}
towers_to_weight = {}
for line in data:
    tower, weight, *subs = re.findall(r'\w+', line)
    towers.append(tower)
    subtowers += subs
    towers_to_subs[tower] = subs
    towers_to_weight[tower] = int(weight)

for tower in towers:
    if tower not in subtowers:
        print('Part 1: ', tower)

def checkWeight(tower):
    subs = towers_to_subs[tower]
    if not subs:
        return towers_to_weight[tower]

    weights = []
    for sub in subs:
        weights.append(checkWeight(sub))

    if weights.count(weights[0]) != len(weights):
        print(tower)
        print(weights)

    total_weight = sum(weights) + towers_to_weight[tower]

    if total_weight == 2166:
        print(tower)
        print(towers_to_weight[tower])
    return total_weight

checkWeight('mwzaxaj')



