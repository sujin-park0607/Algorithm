import hashlib

# #encode => bite로 바꿔줌 
# data = 'test'.encode()
# hash_object = hashlib.sha256()
# hash_object.update(data)
# hex_dig = hash_object.hexdigest() #16진수 변환 

# print(hex_dig)

hash_table = list([0 for i in range(8)])

def get_key(data):
    hash_object = hashlib.sha256()
    hash_object.update(data)
    hex_dig = hash_object.hexdigest()
    return int(hex_dig,16)

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
