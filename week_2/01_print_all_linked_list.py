# [3] -> [4]
# data, next

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


node = Node(3)
first_node = Node(4)
node.next = first_node

class LinkedList:
    def __init__(self, data):
        self.head = Node(data)

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
            return
        self.head.next = Node(data)

        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(data)

linked_list = LinkedList(3)
print(linked_list.head.data)