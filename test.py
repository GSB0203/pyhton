n = int(input())
c = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
remain = n
check = 0

for i in c:
    check += remain//i
    remain = remain%i
    
print(check)