 #힙과 배열 
 #일반적으로 힙 구현시 배열 자료구조를 활용함 
 #부모노드 구하기 = 자식노드 인덱스번호 // 2 
 #왼쪽자식노드 = 인덱스번호 *2 
 #오른족자식노드 = 인덱스번호 * 2 + 1 

from turtle import right


class Heap():
    def __init__(self, data):
        self.heap_array = list()
        self.heap_array.append(None) #인덱스를 1번부터 지칭하기 위함 
        self.heap_array.append(data)

    #부모노드보다 더 클경우 실행되는 함수 
    def move_up(self, inserted_idx):
        if inserted_idx <= 1:
            return False
        parent_idx = inserted_idx //2
        if self.heap_array[inserted_idx] > self.heap_array[parent_idx]:
            return True
        else:
            return False


    #데이터 추가 
    def insert(self, data):
        if len(self.heap_array) == 0:
            self.heap_array.append(None)  
            self.heap_array.append(data)
            return True
        
        self.heap_array.append(data)

        inserted_idx = len(self.heap_array) -1 

        while self.move_up(inserted_idx):
            parent_idx = inserted_idx //2
            #swap
            self.heap_array[inserted_idx], self.heap_array[parent_idx] = self.heap_array[parent_idx],self.heap_array[inserted_idx]
            inserted_idx = parent_idx
        return True


    def move_down(self, poped_idx):
        left_child_popped_idx = poped_idx * 2
        right_child_popped_idx = poped_idx * 2 + 1 
        
        #cas1: 왼쪽 자식 노드도 없을 때 
        if left_child_popped_idx >= len(self.heap_array):
            return False 
        #case2: 오른쪽 자식 노드만 없을때 
        elif right_child_popped_idx >= len(self.heap_array):
            if self.heap_array[poped_idx] < self.heap_array[left_child_popped_idx]:
                return True 
            else: 
                return False

        #case3: 왼쪽, 오른쪽 자식 노드 모두 있을 때
        else:
            if self.heap_array[left_child_popped_idx] > self.heap_array[right_child_popped_idx]:
                if self.heap_array[poped_idx] < self.heap_array[left_child_popped_idx]:
                    return True
                else:
                    return False
            else:
                if self.heap_array[poped_idx] < self.heap_array[right_child_popped_idx]:
                    return True
                else:
                    return False

    def pop(self):
        #데이터가 없는경우 
        if len(self.heap_array) <= 1:
            return None

        returned_data = self.heap_array[1]
        self.heap_array[1] = self.heap_array[-1]
        del self.heap_array[-1]
        poped_idx = 1 

        while self.move_down(poped_idx):
            left_child_popped_idx = poped_idx * 2
            right_child_popped_idx = poped_idx * 2 + 1 
            
            #case2: 오른쪽 자식 노드만 없을때 
            if right_child_popped_idx >= len(self.heap_array):
                if self.heap_array[poped_idx] < self.heap_array[left_child_popped_idx]:
                    self.heap_array[poped_idx],self.heap_array[left_child_popped_idx] = self.heap_array[left_child_popped_idx], self.heap_array[poped_idx]
                    poped_idx = left_child_popped_idx 

            #case3: 왼쪽, 오른쪽 자식 노드 모두 있을 때
            else:
                if self.heap_array[left_child_popped_idx] > self.heap_array[right_child_popped_idx]:
                    if self.heap_array[poped_idx] < self.heap_array[left_child_popped_idx]:
                        self.heap_array[poped_idx],self.heap_array[left_child_popped_idx] = self.heap_array[left_child_popped_idx], self.heap_array[poped_idx]
                        poped_idx = left_child_popped_idx
                else:
                    if self.heap_array[poped_idx] < self.heap_array[right_child_popped_idx]:
                        self.heap_array[poped_idx],self.heap_array[right_child_popped_idx] = self.heap_array[left_child_popped_idx], self.heap_array[poped_idx]
                        poped_idx = right_child_popped_idx

        return returned_data
        

heap = Heap(15)
heap.insert(10)
heap.insert(8)
heap.insert(5)
heap.insert(4)
heap.insert(20)

print(heap.heap_array)

heap.pop()
print(heap.heap_array)

heap.pop()
print(heap.heap_array)

#시간복잡도  O(logn)