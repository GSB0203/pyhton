
#추가 기능 아직 안 만듬
from typing import Self

class CircularQueue:
  def __init__(self, capacity = 5):  #큐 초기화 함수
    self.capacity = capacity  #큐 최대 사이즈
    self.list = [None] * (capacity)  # 큐 요소 저장 리스트
    self.front = -1  #큐 앞부분 가르키는 인덱스 & 초기화
    self.rear = -1  #큐 뒷부분 가르키는 인덱스 & 초기화

  def isEmpty(self):  #큐가 비었는지 확인하는 함수
    return self.front == self.rear  #큐가 비었으면 true, 아니면 false

  def isFull(self):  #큐가 가득 찼는지 확인하는 함수
    return self.rear == self.capacity - 1  #큐가 가득 찼으면 true, 아니면 false

  def enQueue(self, item):  #값 삽입
    if(self.isFull()):  #큐가 가득 찼는가?
      print("큐가 가득 찼습니다.")  #출력
    else:  #아니면
      self.rear += 1  #rear 값 증가
      self.list[self.rear] = item  #rear 위치에 값 저장

  def deQueue(self):  #값 제거
    if(self.isEmpty()):  #큐가 비었는가?
      print("큐가 비어있습니다.")  #출력
    else :  #아니면
      self.front += 1  #front 값 증가
      item = self.list[self.front]  #삭제할 값 itme에 저장
      self.list[self.front] = None  #값이 있던 공간 None 저장
      print(item)  #제거 값 출력
      return item  #제거 값 리턴


  def peek(self):  #가장 처음 값 보기
    if(self.isEmpty()):  #큐가 비었는가?
      print("큐가 비어있습니다.")  #출력
    else:  #아니면
      print(self.list[self.front])  #가장 처음에 있던 값 출력
      return self.list[self.front]  #가장 처음에 있던 값 리턴




queue = CircularQueue()
queue.peek()
queue.enQueue(1)
queue.enQueue(2)
queue.enQueue(3)
queue.enQueue(4)
print(queue.list)
queue.enQueue(5)
queue.peek()
queue.deQueue()
print(queue.list)
queue.enQueue(6)
queue.peek()
queue.deQueue()

print(queue.list)