s = input()
p = str(int(s) + int(s[::-1]))
if p == p[::-1]:
    print("YES")
else:
    print("NO")
