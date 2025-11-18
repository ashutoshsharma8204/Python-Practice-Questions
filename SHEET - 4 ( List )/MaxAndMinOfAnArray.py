A = list(map(int, input("Enter array elements separated by space: ").split()))

max_val = A[0]
min_val = A[0]

for num in A:
    if num > max_val:
        max_val = num
    if num < min_val:
        min_val = num

print("Max value:", max_val)
print("Min value:", min_val)