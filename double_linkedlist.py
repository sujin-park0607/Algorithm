
class Node:
    def __init__(self, data, prev=None, next=None):
        self.prev = prev
        self.data = data
        self.next = next
    
class NodeMgmt:
    def __init__(self,data):
        self.head = Node(data)
        self.tail = self.head

    #데이터 추가 
    def insert(self, data):
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
        else:
            node = self.head
            while node.next:
                node = node.next
            new = Node(data)
            node.next = new
            new.prev = node
            self.tail = new

    #데이터 출력
    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

    #앞에서부터 데이터찾기
    def search_from_head(self, data):
        if self.head == None:
            return False
        
        node = self.head
        while node:
            if node.data == data:
                return node
            else:
                node = node.next
        return False 
    
    #뒤에서부터 데이터찾기
    def search_from_tail(self, data):
        if self.tail == None:
            return False
        
        node = self.tail
        while node:
            if node.data == data:
                return node
            else:
                node = node.prev
        return False

    #특정 노드 앞에 데이터추가 
    def insert_before(self,data, before_data):
        if self.head == None:
            self.head = Node(data)
            return True
        
        node = self.tail
        while node.data != before_data:
            node = node.prev
            if node == None:
                return False
        new = Node(data)
        before_new = node.prev      
        before_new.next = new 
        new.prev = before_new 
        new.next = node

        node.prev = new 

    #특정 노드 뒤에 데이터추가
    def insert_next(self, data, next_data):
        if self.head == None:
            self.head = Node(data)
            return True

        node = self.head
        while node.data != next_data:
            node = node.next
            
            if node == None:
                return False
        new = Node(data)
        next_new = node.next
        next_new.prev = new
        new.next = next_new
        new.prev = node
        node.next = new 


    
double_linked_list = NodeMgmt(0)

for data in range(1,10):
    double_linked_list.insert(data)

# double_linked_list.desc()
# node_3 = double_linked_list.search_from_head(0)
# print(node_3.data)

# node_7 = double_linked_list.search_from_tail(7)
# print(node_7.data)

double_linked_list.insert_before(1.5,2)
double_linked_list.desc()