from random import *

def search(rand_data_list, data):    
    for i in rand_data_list:
        if i == data:
            return True
        else:
            return '-1'

data = int(input())
rand_data_list = list()
for _ in range(10):
        rand_data_list.append(randint(1,100))
print(search(rand_data_list,data))
