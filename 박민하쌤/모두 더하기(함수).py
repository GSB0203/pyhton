
c=list(map(int, input().split()))

def ref(c):
  if len(c)==0:
    return 0
  fin=c.pop()
  return ref(c)+fin

print(ref(c))
  
