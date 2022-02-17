import hashlib

# string = input()

# result = hashlib.sha256(string.encode())
# print(result.hexdigest())


################
input_data = input()
encoded_data = input_data.encode()
result = hashlib.sha256(encoded_data).hexdigest()
print(result)