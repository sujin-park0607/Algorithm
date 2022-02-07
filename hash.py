# hash_table = list([0 for i in range(10)])
# print(hash_table)

# def hash_func(key):
#     return key%5


# def storage_data(data, value):
#     key = ord(data[0])
#     hash_address = hash_func(key)
#     hash_table[hash_address] = value

# def get_data(data): 
#     key = ord(data[0])
#     hash_address = hash_func(key)
#     return hash_table[hash_address]
# data1 = 'Andy'
# data2 = 'Dave'
# data3 = 'Trump'


# storage_data('Andy','0105553333')
# storage_data('Andy','010444333')
# storage_data('Andy','010223333')



# ##ord():문자의 ASCII(아스키) 코드 리턴 
# ## unicode
# print(ord(data1[0]),ord(data2[0]),ord(data3[0]))
# print(hash_func(ord(data1[0])))

##충돌문제 해결 -> Chaining 기법: 링크드리스트로 연결 
# hash_table = list([0 for i in range(8)])

# def get_key(data):
#     return hash(data)

# def hash_function(key):
#     return key % 8

# def save_data(data, value):
#     index_key = get_key(data)
#     hash_address = hash_function(index_key)

#     if hash_table[hash_address] != 0:
#         for index in range(len(hash_table[hash_address])):
#             if hash_table[hash_address][index][0] == index_key:
#                 hash_table[hash_address][index][1] = value
#                 return 
#         hash_table[hash_address].append([index_key,value])
    
#     else:
#         hash_table[hash_address] = [[index_key,value]]

# def read_data(data):
#     index_key = get_key(data)
#     hash_address = hash_function(index_key)

#     if hash_table[hash_address] != 0:
#         for index in range(len(hash_table[hash_address])):
#             if hash_table[hash_address][index][0] == index_key:
#                 return hash_table[hash_address][index][1]
#         return None
#     else:
#         return None
 


 ##충돌문제 해결 - Linear Probing기법 
hash_table = list([0 for i in range(8)])

def get_key(data):
    return hash(data)

def hash_function(key):
    return key % 8

def save_data(data, value):
    index_key = get_key(data)
    hash_address = hash_function(index_key)
    if hash_table[hash_address] != 0:
        for index in range(hash_address, len(hash_table)):
            if hash_table[index] == 0:
                hash_table[index] = [index_key,value]
                return
            #key가 동알하다면 value update작업
            elif hash_table[index][0] == index_key:
                hash_table[index][1] = value
                return
    else:
        hash_table[hash_address] = [index_key,value]


def read_data(data):
    index_key = get_key(data)
    hash_address = hash_function(index_key)

    if hash_table[hash_address] != 0:

        for index in range(hash_address, len(hash_table)):
            if hash_table[index] == 0:
                return None

            elif hash_table[index][0] == index_key:
                return hash_table[index][1]

    else:
        return None

print(hash('dk')%8)
print(hash('dc')%8)

save_data('dk','1201023010')
save_data('dc','1205523010')

print(read_data('Dd'))
print(read_data('Dave'))
print(hash_table)