A = "aabbcc"
B = 98 

target_char = chr(B)

index = A.find(target_char)

if index != -1:
    print(index)
else:
    print("Does not exist") 