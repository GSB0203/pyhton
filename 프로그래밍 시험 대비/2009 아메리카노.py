k, n = map(int, input().split())
sum = 0
while k >= n:
  sum += 1
  k -= n
  k += 1

print(sum)