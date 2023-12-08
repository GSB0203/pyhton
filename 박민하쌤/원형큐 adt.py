#추가 기능 아직 안 만듬
from typing import Self

class CircularQueue:
  def __init__(self, capacity = 5):
    self.capacity = capacity
    self.list = [None] * (capacity)
    self.front = 0
    self.rear = 0

  def isEmpty(self):
    return self.front == self.rear

  def isFull(self):
    return (self.rear + 1) % self.capacity == self.front

  def enqueue(self, item):
    if(self.isFull()):
      print("큐가 가득 찼습니다.")
      pass
    else:
      self.rear = (self.rear + 1) % self.capacity
      self.list[self.rear] = item

  def dequeue(self):
    if(self.isEmpty()):
      print("큐가 비어있습니다.")
      pass
    else :
      self.front = (self.front + 1) % self.capacity
      print(self.list[self.front])
      return self.list[self.front]


  def peek(self):
    if(self.isEmpty()):
      print("큐가 비어있습니다.")
      pass
    else:
      print(self.list[self.rear])
      return self.list[self.front]




queue = CircularQueue()
queue.peek()
queue.enqueue(1)
queue.peek()
queue.enqueue(2)
queue.peek()
queue.enqueue(3)
queue.peek()
queue.enqueue(4)
queue.peek()
print(queue.list)
queue.enqueue(5)
queue.peek()
queue.dequeue()
print(queue.list)
queue.enqueue(6)
queue.peek()

print(queue.list)