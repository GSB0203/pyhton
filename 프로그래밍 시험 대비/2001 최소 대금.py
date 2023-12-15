s = [0] * 3
j = [0] * 2

for i in range(3):
  s[i] = int(input())

for i in range(2):
  j[i] = int(input())

min_s = min(s)
min_j = min(j)

print((min_j + min_s) + ((min_s + min_j) / 10))