#adt 8개 만들기 기본(5) + 3개 정도?

from pyclbr import Class

class Stack:
  def __init__(self, stack_size = 5):  #스택 초기화
    self.stack_size = stack_size  #최대 스택 사이즈 설정
    self.list = [None] * stack_size  #최대 스택 사이즈만큼 리스트 선언
    self.top = -1  #top 초기화

  def isEmpty(self):  #비었는지 확인하는 함수
    return self.top == -1  #top이 가장 마지막에 있는가라면 true, 아니면 false

  def isFull(self):  #가득 찼는지 확인하는 함수
    return self.top == self.stack_size - 1  #top과 최대 스택 사이즈가 같으면 true, 아니면 false

  def push(self, e):  #값 삽입 함수
    if not self.isFull():  #가득 찼지 않았는가?
      self.top += 1  #top 값 증가
      self.list[self.top] = e  #top 위치에 값 삽입
    else:  #가득 찼다면
      print("스택이 가득 찾습니다.")  #출력

  def pop(self):  #값 제거 함수
    if not self.isEmpty():  #비어있지 않은가?
      self.top -= 1  #top 값 감소
      item = self.list[self.top]  #제거된 값 item에 저장
      self.list[self.top] = None  #제거된 값 위치 None 저장
      print(item)  #제거 값 출력
      return item  #제거 값 리턴
    else:  #비어있으면
      print("스택이 비어있습니다.")  #출력

  def peek(self):  #가장 위에 있는 값 출력 함수
    if not self.isEmpty():  #비어있지 않은가?
      item = self.list[self.top]  #제거된 값 item에 저장
      print(item)  #제거 값 출력
      return item  #제거 값 리턴
    else:  #비어있으면
      print("스택이 비어있습니다.")  #출력

  #추가 기능

  def allPrint(self):  #전부 출력 함수
    if not self.isEmpty():  #비어있지 않은가?
      print(self.pop())  #pop 실행하여 값 제거
      self.allPrint()  #재귀 함수로 값 비어있을 때가지 실행
    else:  #비어있으면
      print("스택이 비어있습니다.")  #출력

  def nowStackSize(self):  #현재 스택 사이즈 출력 함수
    print("Stack size : {}".format(self.top + 1))  #현재 값이 들어있는 위치 = 현재 스택 사이즈 출력
    return self.top + 1  #현재 값이 들어있는 위치 = 현재 스택 사이즈 리턴
    
  def search(self, key):  #원하는 값 찾는 함수
    if not self.isEmpty():  #비어있지 않은가?
      for i in range(self.top + 1):  #스택 사이즈 만큼 반복
        if(self.list[i] == key):  #찾는 값이 존재하는가?
          print("입력된 값이 존재합니다.")  #출력
          return key  #찾는 값 리턴
      print("스택이 비어있습니다.")  #출력
    else:  #비었는가
      print("입력된 값이 존재하지 않습니다.")  #없으면 출력

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.search(3)
stack.pop()
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
