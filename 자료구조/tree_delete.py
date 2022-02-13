#########1.삭제할 Node의 오른쪽 자식중, 가장 작은 값을 삭제할 Node의 Parent Node가 가리키게 할 경우
#-삭제할 Node의 오른쪽 자식 선택
# -오른쪽 자식의 가장 왼쪽에 있는Node를 선택
# -해당 Node를 삭제할 Node의 Parent Node의 왼쪽 Branch가 가르키게 함 
# -해당 Node의 왼쪽 Branch가 삭제할 Node의 왼쪽 Child Node를 가르키게 함
# -해당 Node의 오른쪽 Branch가 삭제할 Node의 오른쪽 Child Node를 가르키게 함
# -만약 해당 Node 가 오른쪽 Child Node를 가지고 있었을 경우에는, 해당 Node의 본래 Parent Node의 왼쪽 
# Branch가 해당 오른족 Child Node를 가르키게 함 

import random

#노드 클래스 만들기
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

#이진 탐색 트리에 데이터 넣기
class NodeMgmt:
    def __init__(self, head):
        self.head = head

    #노트 추가 함수
    def insert(self,value):
        self.current_node = self.head
        while True:
            if value < self.current_node.value:
                if self.current_node.left != None:
                    self.current_node = self.current_node.left
                else:
                    self.current_node.left = Node(value)
                    break

            else:        
                if self.current_node.right != None:
                    self.current_node = self.current_node.right
                else:
                    self.current_node.right = Node(value)
                    break

    #특정 노드가 있는지 확인하는 함수
    def search(self, value):
        self.current_node = self.head
        while self.current_node:
            if self.current_node.value == value:
                return True
            elif value < self.current_node.value:
                self.current_node = self.current_node.left
            else:
                self.current_node = self.current_node.right

        return False

    def delete(self,value):
        searched = False
        self.current_node = self.head
        self.parent = self.head
        while self.current_node:
            if self.current_node == value:
                searched = True
                break
            elif value < self.current_node.value:
                self.parent = self.current_node
                self.current_node = self.current_node.left
            else:
                self.parent = self.current_node
                self.current_node = self.current_node.right
        
        if searched == False:
            return False

        #이후부터 Case 들을 분리해서, 코드 작성 

        #Case1. Leaf Node인 경우 

        #self.current_node 가 삭제할 Node, self.parent는 삭제할 Node의 parent NOde인 상태
        if self.current_node.left == None and self.current_node.right == None:
            if value < self.parent.value:
                self.parent.left == None
            else:
                self.parent.right == None
            del self.current_node


        #Case2. 삭제할 노드가 Child Node가 한개인 경우 

        #왼쪽에만 노드존재
        elif self.current_node.left != None and self.current_node.right == None:
            if value < self.parent.value:
                self.parent.left = self.current_node.left
            else:
                self.parent.right = self.current_node.left
        #오른쪽에만 노드 존재 
        elif self.current_node.left == None and self.current_node.right != None:
            if value < self.parent.value:
                self.parent.left = self.current_node.right
            else:
                self.parent.right = self.current_node.right
        

        #Case3. 삭제할 노드가 Child NOde를 두개 가지고 있을 경우
        elif self.current_node.left != None and self.current_node.right != None:
            #Case3-1
            if value < self.parent.value:
                self.change_node = self.current_node.right
                self.change_node_parent = self.current_node.right

                while self.change_node.left != None:
                    self.change_node_parent = self.change_node
                    self.change_node = self.change_node.left

                #change_node 의 Child_node가 있을경우
                if self.change_node.right != None:
                    self.change_node_parent.left = self.change_node.right
                
                #change_node 의 Child_node가 없을경우
                else:
                    self.change_node_parent.left = None

                self.parent.left = self.change_node
                self.change_node.right = self.current_node.right
                self.change_node.left = self.change_node.left
            #Case3-2
            else:
                self.change_node = self.current_node.right
                self.change_node_parent = self.current_node.right
                while self.change_node.left != None:
                    self.change_node_parent = self.change_node
                    self.change_node = self.change_node.left
                
                #change_node의 Child_node가 있을경우
                if self.change_node.right != None:
                    self.change_node_parent.left = self.change_node.right
                else:
                    self.change_node_parent.left = None
                self.parent.right = self.change_node
                self.change_node.left = self.current_node.left
                self.change_node.right = self.current_node.right

        return True

# 0~999 숫자 중에서 임의로 100개를 추출해서, 이진 탐색 트리에 입력, 검색, 삭제
bst_nums = set() #중복방지를 위한 set으로 진행 
while len(bst_nums) != 100:
    bst_nums.add(random.randint(0,999))

#선택된 100개의 숫자를 이진탐색트리에 입력, 임의로 루트노드는 500을 넣기로함
head = Node(500)
binary_tree = NodeMgmt(head)
for num in bst_nums:
    binary_tree.insert(num)

#입력한 100개의 숫자 검색(검색 기능 확인)
for num in bst_nums:
    if binary_tree.search(num) == False:
        print("search failed")
    # else:
    #     print("True")
#100개의 숫자 중 10개의 숫자를 랜덤 선택
delete_nums = set()
bst_nums = list(bst_nums)
while len(delete_nums) != 10:
    delete_nums.add(bst_nums[random.randint(0,99)])

print(delete_nums)
#선택한 10개의 숫자를 삭제(삭제 기능 확인)
for del_num in delete_nums:
    if binary_tree.delete(del_num) == False:
        print('delete failed', del_num)


#시간복잡도
#O(logN)




            


             




            



