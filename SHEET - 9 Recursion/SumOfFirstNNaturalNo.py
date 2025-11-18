n = int(input("Enter a positive integer: "))
def sum_of_natural_numbers(n):
    if n == 1:
        return 1
    else:
        return n + sum_of_natural_numbers(n - 1)
print("The sum of the first", n, "natural numbers is:", sum_of_natural_numbers(n))