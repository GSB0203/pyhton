n=int(input())
num=list(map(int, input().split()))
result= list(0 for _ in range(24))


for i in range(n):
   result[num[i]]+=1
    
for i in range(1, 24):
   print(result[i], end=' ')
