from typing import Self


class CircularQueue:
  def __init__(self, capacity = 5):
    self.capacity = capacity
    self.list = [None] * capacity
    self.front = 0
    self.rear = 0

def isEmpty(self):
  return self.front == self.rear

def isFull(self):
  return self.rear == self.capacity - 1

def enqueue(self, item):
  if(isFull(self)):
    print("큐가 가득 찼습니다.")
  
  else:
    self.rear = (self.rear + 1) %self.capacity
    self.list[self.rear] = item

def dequeue(self):
  if(isEmpty(self)):
    print("큐가 비어있습니다.")

  else :
    self.front = (self.front + 1) % self.capacity
    print(self.list[self.front])


def peek(self):
  if(isEmpty(self)):
    print("큐가 비어있습니다.")
  else:
    print(self.list[self.rear])


queue = CircularQueue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
queue.dequeue()
queue.dequeue()
queue.enqueue(6)