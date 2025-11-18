rows = int(input("Enter number of rows: "))

# Top half
for i in range(1, rows + 1):
    print("*" * i)

# Bottom half
for i in range(rows - 1, 0, -1):
    print("*" * i)