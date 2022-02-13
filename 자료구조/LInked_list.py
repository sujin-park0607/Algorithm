class Node():

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class NodeMgmt():

    def __init__(self, data):
        self.head = Node(data)
    
    def add(self,data):
        if self.head == None:
            self.head == Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data)
    
    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

    def delete(self, data):
        if self.head == data:
            print("노드가 없어요")
            return
        
        if self.head.data == data:
            temp = self.head
            self.head = self.head.next
            del temp
        
        else:
            node = self.head
            while node.next:
                if node.next == data:
                    temp = node.next
                    node.next = node.next.next
                    del temp
                else:
                    node = node.next




linkedlist = NodeMgmt(0)

for data in range(1,10):
    linkedlist.add(data)

linkedlist.desc()

linkedlist.delete(1)
print('------------------------')
linkedlist.desc()