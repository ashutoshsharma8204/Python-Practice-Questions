A = list(map(int, input("Enter array elements separated by space: ").split()))

for num in A:
    if num < 0:
        print(num)