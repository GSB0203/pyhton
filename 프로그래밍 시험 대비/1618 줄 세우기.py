s = list(map(int, input().split()))

  #첫번째 방법 : sort
s.sort()
print(*s)

  #두번째 방법 : sorted
s_re = sorted(s)
print(*s_re)