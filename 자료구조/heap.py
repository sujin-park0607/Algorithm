 #힙과 배열 
 #일반적으로 힙 구현시 배열 자료구조를 활용함 
 #부모노드 구하기 = 자식노드 인덱스번호 // 2 
 #왼쪽자식노드 = 인덱스번호 *2 
 #오른족자식노드 = 인덱스번호 * 2 + 1 


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

        

heap = Heap(15)
heap.insert(10)
heap.insert(8)
heap.insert(5)
heap.insert(4)
heap.insert(20)

print(heap.heap_array)