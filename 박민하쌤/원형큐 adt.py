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

  def reverseDeQueue(self):  #마지막 제거하는 함수
    if not self.isEmpty():  #비어있지 않았는가?
      item = self.list[self.rear]  #item에 제거되는 맨 뒤 값 저장
      self.list[self.rear] = None  #맨 뒤 값 제거
      self.rear -= 1  #공간 이동
      print(item)  #제거 값 출력
      return item  #제거 값 리턴
    else:  #비어있으면
      print("큐가 비어있습니다.")  #출력

  def search(self, key):  #값 찾기 함수
    if not self.isEmpty():  #비어있지 않은가?
      for i in range(self.capacity):  #현재 큐 최대 사이즈만큼 반복
        if(self.list[i] == key):  #찾는 값이 존재하는가?
          print("입력된 값이 존재합니다.")  #출력
          return key  #찾는 값 리턴
      print("입력된 값이 존재하지 않습니다.")  #없으면 출력
    else:  #비었는가      
      print("스택이 비어있습니다.")  #출력

  def reomveKey(self, key):
    if not self.isEmpty():  #비어있지 않은가?
      for i in range(self.capacity):  #현재 큐 최대 사이즈만큼 반복
        if(self.list[i] == key):  #찾는 값이 존재하는가?
          item = self.list[i]  #찾은 값 item에 저장
          self.list[i] = None  #찾은 값이 있던 공간 삭제
          print(item)  #찾은 값 출력
          return item  #찾은 값 리턴
      print("제거할 값이 없습니다.")  #출력
    else:  #비어있으면
      print("큐가 비어있습니다.")  #출력



queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
queue.peek()
queue.dequeue()
print(queue.list)
queue.enqueue(6)
queue.search(6)
queue.search(1)
queue.peek()
queue.reverseDeQueue()
queue.reomveKey(4)
queue.enqueue(1)
print(queue.list)