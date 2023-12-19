  #재귀함수
def gcd(a, b, cnt):
  if b <= 0:
    return a
  print(cnt)
  cnt += 1
  return gcd(b, a%b, cnt)

a, b =map(int, input().split())
cnt = 0
print(gcd(a, b, cnt))
  #cnt 2번작동

def gcd(a, b, cnt):
  if a % b == 0:
    return b
  print(cnt)
  cnt += 1
  return gcd(b, a%b, cnt)

a, b =map(int, input().split())
cnt = 0
print(gcd(a, b, cnt))
  #cnt 3번 작동

  #반복문
a, b = map(int, input().split())
cnt = 0
while(b > 0):
  a, b = b, a%b
  print(cnt)
  cnt += 1
print(a)

  #cnt 3번 작동