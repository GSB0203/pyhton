
#추가 기능 아직 안 만듬
from typing import Self

class CircularQueue:
  def __init__(self, capacity = 5):
    self.capacity = capacity
    self.list = [None] * (capacity)
    self.front = -1
    self.rear = -1

  def isEmpty(self):
    return self.front == self.rear

  def isFull(self):
    return self.rear == self.capacity - 1

  def enQueue(self, item):
    if(self.isFull()):
      print("큐가 가득 찼습니다.")
      pass
    else:
      self.rear += 1
      self.list[self.rear] = item

  def deQueue(self):
    if(self.isEmpty()):
      print("큐가 비어있습니다.")
      pass
    else :
      self.front += 1
      print(self.list[self.front])
      return self.list[self.front]


  def peek(self):
    if(self.isEmpty()):
      print("큐가 비어있습니다.")
      pass
    else:
      print(self.list[self.front])
      return self.list[self.front]




queue = CircularQueue()
queue.peek()
queue.enQueue(1)
queue.peek()
queue.enQueue(2)
queue.peek()
queue.enQueue(3)
queue.peek()
queue.enQueue(4)
queue.peek()
print(queue.list)
queue.enQueue(5)
queue.peek()
queue.deQueue()
print(queue.list)
queue.enQueue(6)
queue.peek()

print(queue.list)