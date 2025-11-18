A = list(map(int, input("Enter array elements separated by space: ").split()))

even_count = 0
odd_count = 0

for num in A:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print(abs(even_count - odd_count))