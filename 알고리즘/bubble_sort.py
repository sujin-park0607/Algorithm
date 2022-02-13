#데이터가 2개

# for index in range(데이터길이 -1):
#     for index2 in range(데이터길이 - index -1):
#         if 앞데이터 > 뒤데이터:
#             swap(앞, 뒤)

import random

def bubblesort(data):
    for index in range(len(data)-1):
        swap = False
        for index2 in range(len(data)-index-1):
            if data[index2]> data[index2+1]:
                data[index2],data[index2+1] = data[index2+1],data[index2]
                swap = True
        
        if swap == False:
            break
    return data

data_list = random.sample(range(100),50)
print(bubblesort(data_list))