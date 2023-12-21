from pyclbr import Class
global index 
index = 0
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

def precedence(op):  #연산자의 우선순위를 매기기 위한 함수
  if op == '*' or op == '/': return 2  #'*', '/' 인가 2 리턴
  elif op == '+' or op == '-': return 1  #'+', '-' 인가 1 리턴
  elif op == '(' or op == ')': return 0  # '(', ')' 인가 0 리턴
  else: return -1  #그 외에는 -1 리턴

def Infix2Postfix(expr):  #중위를 후위로 바꾸기 위한 함수
  s = Stack(100)  #연산자를 계산하기 위한 s(stack)
  output = []  #연산값을 저장하기 위한 output(list)

  for term in expr:  #expr(list) 만큼 term 반복
    if term in '(':  #term 이 '(' 인가
      s.push(term)  #s(stack)에 term 추가

    elif term in ')':  #term 이 ')' 인가
      while not s.isEmpty():  #s(stack) 이 빈공간일 때까지 반복
        op = s.pop()  #op라는 변수에 s(stack)에 top값 저장
        if op == '(':  #만약 op가 '(' 인가
          break  #반복 멈춤
        else:  #빈공간인가
          output.append(op)  #append 를 이용하여 output(리스트) 마지막에 op값 추가
    elif term in "*/+-":  #연산자인가
      while not s.isEmpty():  #빈공간이 아닌가
        op = s.peek()  #op 변수에 s(stack)의 top값 저장(but 내보내진 않음) 이유 : 우선순위를 모르는 상황에서 그냥 내보내는건 위험해서
        if (precedence(term) < precedence(op)):  #우선순위가 op가 더 큰가?
          output.append(op)  #output(리스트) 마지막에 op 값 추가
          s.pop()  #s(stack) top값 내보냄
        else: break  #아니면 반복 멈춤
      s.push(term)  #비교 후 남은 연산자 s(stack) 추가
    else:  #그 외의 경우(피연산자인 경우)
      output.append(term)  #output(리스트) 마지막에 피연산자값 추가
  
  while not s.isEmpty():  #마지막으로 아직 s(stack)에 값이 남아있는가?
    output.append(s.pop())  #남아있는 값 output(리스트) 마지막에 pop값 추가
  
  return output  #찐마지막 output(리스트) 값 리턴

infix1 = input()
infix1 = list(infix1)
postfix1 = (Infix2Postfix(infix1))
print(postfix1)