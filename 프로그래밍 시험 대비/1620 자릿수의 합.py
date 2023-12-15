#문제만 보고 못 푼 문제들 중 하나
n = int(input())
sum = 0
while sum == 0 or sum >= 10:
  sum = 0
  while n > 0:
    sum += int(n % 10)
    n = int(n / 10)
  n = sum

print(sum)