class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class NodeMgmt:
    def __init__(self, data):
        self.head = Node(data)

    def add(self, data):
        #방어코드 헤드값이 없다면 추가할데이터는 head값 가진다
        if self.head == "":
            self.head = Node(data)
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
    
    def delete(self,data):
        #방어코드
        if self.head == "":
            print("해당 값을 가진 노드가 없습니다.")
            return
        
        #삭제 데이터가 head인경우 
        if self.head.data == data:
            temp = self.head 
            self.head = self.head.next
            del temp
        #마지막노드, 중간노드 삭제 
        else:
            node = self.head
            while node.next:
                if node.next.data == data:
                    temp = node.next
                    node.next = node.next.next
                    del temp
                    return
                else:
                    node = node.next



linkedlist1 = NodeMgmt(0)

for i in range(1,10):
    linkedlist1.add(i)
linkedlist1.desc()

print("----------")

linkedlist1.delete(4)
linkedlist1.desc()