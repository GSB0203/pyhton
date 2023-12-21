  #타입 확인
int1 = 5  #타입 int
boolean = True  #타입 bool
string = "bssm"  #타입 str
float = 5.5  #타입 float
list = [10, 20, 30, 40]  #타입 list
tuple = (10, 20)  #타입 tuple
tuple2 = (10)  #값이 하나만 존재할 경우 tuple 도 타입은 int이다.
dict = {1:10}  #타입 dict
set = {20}  #타입 set

print(type(int1))  #<class 'int'>
print(type(boolean))  #<class 'bool'>
print(type(string))  #<class 'str'>
print(type(float))  #<class 'float'>
print(type(list))  #<class 'list'>
print(type(tuple))  #<class 'tuple'>
print(type(tuple2))  #<class 'int'>
print(type(dict))  #<class 'dict'>
print(type(set))  #<class 'set'>

#----------------------------------------------------

  #list 컴프리헨션로 초기화 & 출력
arr = [x for x in range(10)]
print(arr)

  #list 슬라이싱
print(arr[1:3])
print(arr[:3])
print(arr[1:])
 
#----------------------------------------------------

  #반복문 흐름 따라가기
n, m = map(int, input().split())
for i in range(n, m, 1):
  for j in range(i + m, i, -1):
    print(i, j)

#----------------------------------------------------

  #조건문 if, elif

#----------------------------------------------------

  #각종 연산자 / ++, -- 불가능, +=, -= 가능
print(5 / 2)  #나머지까지
print(5 // 2)  #목만
print(5 % 2)  #나머지만

#----------------------------------------------------

  #list 정렬(기본 오름차순)
a = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
  #첫번째 방법 : 배열 a 자체를 정렬
a.sort()

  #두번째 방법 : 정열된 배열을 반환하여 변수에 저장
a2 = sorted(a)

  #번외 : 내림차순 정렬하는 방법
re_a = sorted(a, reverse = True)

print(a)
print(a2)
print(re_a)

#----------------------------------------------------

  #list 역출력
a_reverse =''
a = input()
  #첫번째 방법
print(a[::-1])

  #두번째 방법
for i in a:
  a_reverse = i + a_reverse
print(a_reverse)

#----------------------------------------------------

  #코드업 대표 문제 - 약수 구하기(유클리드) 반복, 재귀
  #재귀함수
def gcd(a, b, cnt):
  if b <= 0:
    return a
  print(cnt)
  cnt += 1
  return gcd(b, a%b, cnt)

a, b =map(int, input().split())
cnt = 0
print(gcd(a, b, cnt))
  #cnt 2번작동


def gcd(a, b, cnt):
  if a % b == 0:
    return b
  print(cnt)
  cnt += 1
  return gcd(b, a%b, cnt)

a, b =map(int, input().split())
cnt = 0
print(gcd(a, b, cnt))
  #cnt 3번 작동


  #반복문
a, b = map(int, input().split())
cnt = 0
while(b > 0):
  a, b = b, a%b
  print(cnt)
  cnt += 1
print(a)

  #cnt 3번 작동

  #코드업 3, 4, 5, 6차시 메인
  #ex) 1 ~ n 까지 출력, n ~ 1 까지 출력
#----------------------------------------------------

  #문자열 길이 구하기
n = input()
print(len(n))

#----------------------------------------------------

  #재귀 함수 많이 나옴

#----------------------------------------------------

  #클래스 개념
  #내부 요소
  #메서드란
  #객체란

  #객체 생성
  #객체 이름 = 클래스()

  #클래스 상속
  #class A():
  #class B(A):

#----------------------------------------------------

  #자료구조 스택, 후위표기식, 선형큐, 원형큐, 선형덱, 원형덱 등
  #adt 빈칸 채우기
  #후위표기식 나타내기
  #전위 순회
  #중위 순회
  #후위 순회
class ArrayStack :
    def __init__(self, capacity):
        self.capacity = capacity
        self.array = [None]*self.capacity
        self.top = -1

    def isEmpty(self) :
        return self.top == -1
   
    def isFull (self):
        return self.top == self.capacity
   
    def push(self, e):
        if not self.isFull():
            self.top += 1
            self.array[self.top] = e
        else: pass

    def pop( self ):
        if not self.isEmpty():
            self.top -= 1
            return self.array[self.top+1]
        else: pass

    def peek(self):
        if not self.isEmpty():
            return self.array[self.top]
        else: pass

def precedence(op):
    if op=='(' or op==')': return 0
    elif op=='+' or op=='-': return 1
    elif op=='*' or op=='/': return 2
    else : return -1

def Infix2Postfix (expr):
    s = ArrayStack(100)
    output = []
    for term in expr :
        if term in '(':
            s.push('(')

        elif term in ')':
            while not s.isEmpty():
                op = s.pop()
                if op=='(':
                    break
                else:
                    output.append(op)
        elif term in "+-*/":
            while not s.isEmpty() :
                op = s.peek()
                if( precedence(term) <= precedence(op)):
                    output.append(op)
                    s.pop()
                else: break
            s.push(term)
        else:
            output.append(term)

    while not s.isEmpty() :
        output.append(s.pop())
    return output


from pyclbr import Class
global index 
index = 0

infix1 = input()
infix1 = list(infix1)
postfix1 = (Infix2Postfix(infix1))
print(postfix1)

#----------------------------------------------------

  #각 코드별 수행 횟수 구하기
for i in range(5):  #보기에는 5번이지만 실제로는 6번 수행 but, 시험에는 이건 안 나온다.
   if i % 2 == 0:  #5번 
      print(i)  #2번