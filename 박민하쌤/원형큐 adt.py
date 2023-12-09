#추가 기능 아직 안 만듬
from typing import Self

class Queue:
  def __init__(self, capacity = 5):  #큐 초기화 함수
    self.capacity = capacity  #큐 최대 사이즈 설정
    self.list = [None] * (capacity)  #큐 최대 사이즈 만큼 리스트 선언
    self.front = 0  #큐 앞부분 가르키는 인덱스 & 초기화
    self.rear = 0  #큐 뒷부분 가르키는 인덱스 & 초기화


  def isEmpty(self):  #비었는지 확인하는 함수
    return self.front == self.rear  #front와 rear가 같은 위치이면 true, 아니면, false

  def isFull(self):  #가득 찼는지 확인하는 함수
    return (self.rear + 1) % self.capacity == self.front  #rear에 다음 위치와 front가 같으면 true, 아니면 false

  def enqueue(self, item):  #값 삽입 함수
    if(not self.isFull()):  #가득 차지 않았는가?
      self.rear = (self.rear + 1) % self.capacity  #rear 다음 삽입 공간으로 이동
      self.list[self.rear] = item  #rear 위치에 값 삽입
    else:  #가득찼으면
      print("큐가 가득 찼습니다.")  #출력

  def dequeue(self):  #값 삭제 함수
    if(not self.isEmpty()):  #비어있지 않은가?
      self.front = (self.front + 1) % self.capacity  #front 다음 삭제 공간으로 이동
      item = self.list[self.front]  #item에 삭제 값 저장
      self.list[self.front] = None  #삭제 값 저장된 위치 None 저장
      print(item)  #삭제 값 출력
      return item  #삭제 값 리턴
    else :  #비어있으면
      print("큐가 비어있습니다.")  #출력


  def peek(self):  #가장 끝에 있는 값 출력 함수
    if(not self.isEmpty()):
      item = self.list[self.front]  #item에 삭제 값 저장
      print(item)  #삭제 값 출력
      return item  #삭제 값 리턴
    else:  #비어있으면
      print("큐가 비어있습니다.")  #출력



queue = Queue()
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