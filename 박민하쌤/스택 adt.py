stack_size = 5
list = [None] * stack_size
top = -1

def isEmpty():
  return top == -1

def isFull():
  return top == stack_size - 1

def push(e):
  global top
  if isFull():
    print("스택이 가득 찾습니다.")
    exit()
  else:
    top += 1
    list[top] = e
    print(list)

def pop():
  global top
  if isEmpty():
    print("스택이 비어있습니다.")
    exit()
  else:
    top -= 1
    return list[top+1]
    

def peek():
  if not isEmpty():
    return list[top]
  else: pass



push(1)
push(2)
push(3)
push(4)
push(5)

print(pop())
print(peek())