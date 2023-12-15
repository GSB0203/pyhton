def f(n, m):
  if n > m:
    return
  if n % 2 != 0:
    print(n, end=" ")
  f(n + 1, m)

n, m = map(int, input().split())
f(n, m)