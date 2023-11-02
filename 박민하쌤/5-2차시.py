def jump(n, s=[]):
  if n<1:
    return 0
  elif n==1:
    return 1
  else:
    return 



n=int(input())
s=[int(input()) for _ in range(n)]
dp=[0]*(n)