class Deque:
    def __init__(self, capacity):
        self.capacity = capacity  # 덱 최대 사이즈
        self.list = [None] * capacity  # 덱 요소 저장 리스트
        self.front = 0  # 덱 앞부분 가르키는 인덱스 & 초기화
        self.rear = 0   # 덱 뒷부분을 가리키는 인덱스 & 초기화

    
    def isEmpty(self):  #덱이 비었는지 확인하는 함수
        return self.front == self.rear  #front와 rear가 같은가? true, 아니면 false
    
    def isFull(self):  #덱이 가득 찼는지 확인하는 함수
        return self.front == (self.rear+1)%self.capacity  #front와 그 다음 채울 공간이 가득 찼는가? true, 아니면 false
    
    def addFront(self, e):  #front에서 값 삽입 함수
        if not self.isFull():  #가득 차지 않았는가?
            self.list[self.rear] = e  #현재 rear 위치에 입력받은 값 삽입
            self.rear += 1  #rear값 증가
        else:  #가득 찼다면
            print("덱이 가득 찼습니다.")  #출력
    
    def deleteFront(self):  #front에서 값 제거 함수
        if not self.isEmpty():  #비어있지 않은가?
            self.rear -= 1  #rear를 하나 낮춤
            item =  self.list[self.rear]  #삭제할 값을 item 저장
            self.list[self.rear] = None  #값이 있던 공간 None 저장
            print(item)  #제거 값 출력
            return item  #제거된 요소 리턴
        else:  #비었다면
            print("덱이 비어있습니다.")  #출력
    
    def addRear(self, e):  #rear에서 값 삽입 함수
        if not self.isFull():  #가득 차지 않았다면
            self.front -= 1  #front값 낮추고
            self.list[self.front] = e  #현재 front 위치에 입력받은 값 삽입
        else:  #가득찼다면
            print("덱이 가득 찼습니다.")  #출력

    def deleteRear(self):  #rear에서 값 제거 함수
        if not self.isEmpty():  #비어있지 않다면
            item =  self.list[self.front]  #삭제할 값을 item 저장
            self.list[self.front] = None  #값이 있던 공간 None 저장
            self.front +=  1  #front 다음 공간 지정
            print(item)  #제거된 값 출력
            return item  #제거된 요소 리턴
        else:  #비었다면
            print("덱이 비어있습니다.")  #출력


queue = Deque(5)

queue.addFront(1)
queue.addFront(2)
queue.addRear(3)
queue.addRear(4)
queue.addRear(5)


print(queue.list)

queue.deleteRear()

print(queue.list)

queue.deleteFront()

print(queue.list)
