A = list(map(int, input("Enter array elements separated by space: ").split()))
B = int(input("Enter integer B: "))

found = 0
for num in A:
    if num == B:
        found = 1
        break

print(found)