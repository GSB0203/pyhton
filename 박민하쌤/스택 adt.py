#adt 8개 만들기 기본(5) + 3개 정도?

from pyclbr import Class
from typing import Self

class Stack:
  def __init__(self, stack_size = 5):
    self.stack_size = stack_size
    self.list = [None] * stack_size
    self.top = -1

  def isEmpty(self):
    return self.top == -1

  def isFull(self):
    return self.top == self.stack_size - 1

  def push(self, e):
    if not self.isFull():
      self.top += 1
      self.list[self.top] = e
    else:
      print("스택이 가득 찾습니다.")
      pass

  def pop(self):
    if not self.isEmpty():
      self.top -= 1
      return self.list[self.top + 1]
    else:
      print("스택이 비어있습니다.")
      pass

  def peek(self):
    if not self.isEmpty():
      return self.list[self.top]
    else:
      print("스택이 비어있습니다.")
      pass

  def allPrint(self):
    if not self.isEmpty():
      print(self.pop())
      self.allPrint()
    else:
      print("스택이 비어있습니다.")
      pass

  def nowStackSize(self):
    print("Stack size : {}".format(self.top + 1))
    return self.top + 1
    
  def search(self, key):
    if self.isEmpty():
      print("스택이 비어있습니다.")
      pass
    for i in range(self.top + 1):
      if(self.list[i] == key):
        print("입력된 값이 존재합니다.")
        return key
    print("입력된 값이 존재하지 않습니다.")
    pass


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.search(3)
stack.push(6)
stack.search(6)
stack.nowStackSize()
stack.allPrint()
stack.nowStackSize()

#print(stack.peek())
#print(stack.pop())
#print(stack.pop())
#print(stack.pop())
#print(stack.pop())
#print(stack.pop())
#print(stack.pop())
#print(stack.pop())
