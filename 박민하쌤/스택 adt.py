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
      print(self.list)
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

  def allprint(self):
    if not self.isEmpty():
      print(self.pop())
      self.allprint()
    else:
      print("스택이 비어있습니다.")
      pass
    


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.push(6)

stack.allprint()

#print(stack.peek())
#print(stack.pop())
#print(stack.pop())
#print(stack.pop())
#print(stack.pop())
#print(stack.pop())
#print(stack.pop())
#print(stack.pop())
