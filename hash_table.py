hash_table = list([i for i in range(10)])
hash_table

def hash_func(key):
    return key % 5

def storage_data(data, value):
    key = ord(data[0])
    hash_address = hash_func(key)
    hash_table[hash_address] = value

def get_data(data):
    key = ord(data[0])
    hash_address = hash_func(key)
    return hash_table[hash_address]


storage_data('Andy', '01055553333')
storage_data('Dave', '01044443333')
storage_data('Trump', '01022223333')

print(get_data('Andy'))
print(get_data('Dave'))
print(get_data('Trump'))
