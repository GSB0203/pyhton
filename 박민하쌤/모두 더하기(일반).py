a=[int(input()) for _ in range(5)]
sum=0
for i in range(5):
  sum+=a[i]
print(sum)

b=list(map(int, input().split()))
sum2=0

for i in range(5):
  sum2+=b[i]
print(sum2)