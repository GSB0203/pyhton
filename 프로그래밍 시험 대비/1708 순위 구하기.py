n = int(input())
arr = list(map(int, input().split()))
rank = [1] * n

for i in range(n):
  for j in range(n):
    if arr[i] < arr[j]:
      rank[i] += 1

for i in range(n):
  print(arr[i], rank[i])

