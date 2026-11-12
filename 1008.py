class Node():
    def init (self):
        self.data=None
        self.link=None

node1 = Node()
node1.data = "다현0"

node2 = Node()
node2.data = "다현1"
node1.link = node2

node3 = Node()
node2.data = "다현2"
node1.link = node3

node4 = Node()
node2.data = "다현3"
node1.link = node4

node5 = Node()
node2.data = "다현4"
node1.link = node5

newNode = Node()
newNode.data = "솔라"
newNode.link = node2.link
node2.link = newNode

current = node1
print(current.data, end="   ")
while current.link != None:
    current = current.link
    print(current.data, end="   ")