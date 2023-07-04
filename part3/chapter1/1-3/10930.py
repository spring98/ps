import hashlib

input_data = input()
print(hashlib.sha256(input_data.encode()).hexdigest())

