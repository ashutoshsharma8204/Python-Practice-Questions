A = list(map(int, input("Enter array elements separated by space: ").split()))
B = int(input("Enter integer B: "))

Arr = [x + B for x in A]

print("Output:")
print(Arr)