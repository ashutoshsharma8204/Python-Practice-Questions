A = list(map(int, input().split()))

odds = []
evens = []

for num in A:
    if num % 2 == 0:
        evens.append(str(num))
    else:
        odds.append(str(num))

print(" ".join(odds))
print(" ".join(evens))