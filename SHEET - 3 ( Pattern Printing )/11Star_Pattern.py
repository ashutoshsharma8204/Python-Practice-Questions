rows = int(input("Enter number of rows (odd number recommended): "))

# Top half
for i in range(rows, 0, -1):
    if i > rows // 2 + 1:
        print("*" * i + " " * (2 * (rows - i)) + "*" * i)
    else:
        print("*" * i + " " * (2 * (rows - i)) + "*" * i)

# Bottom half
for i in range(2, rows + 1):
    if i > rows // 2 + 1:
        print("*" * i + " " * (2 * (rows - i)) + "*" * i)
    else:
        print("*" * i + " " * (2 * (rows - i)) + "*" * i)