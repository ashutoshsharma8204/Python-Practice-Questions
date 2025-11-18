n = int(input())
deadline = list(map(int, input().split()))
k = int(input())

count = 0
for i in range(n):
    for j in range(i + 1, n):
        if deadline[i] + deadline[j] == k:
            count += 1
print(count)