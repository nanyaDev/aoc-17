ss = 349

class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None

class CircularList:
    def __init__(self, data):  
        headNode = Node(data)
        headNode.next = headNode

        self.head = headNode

    def traverse(self, startNode, steps):
        curr = startNode
        for _ in range(steps):
          curr = curr.next

        return curr 
  
    def insert(self, node, data):
        newNode = Node(data)

        newNode.next = node.next
        node.next = newNode

        return newNode
  
    def print(self):
        current = self.head

        while(current):
            print(current.data)
            current = current.next

ll = CircularList(0)
curr = ll.head

for i in range(1, 2018):
    curr = ll.traverse(curr, ss)
    curr = ll.insert(curr, i)

print('Part 1:', curr.next.data)

ans = 0
pos = 0
for i in range(1, 50_000_000 + 1):
    pos = (pos + ss) % i

    if pos == 0:
        ans = i

    pos += 1

print('Part 2:', ans)
    


