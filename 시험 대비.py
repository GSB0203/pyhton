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
print(type(tuple))  #<class 'int'>
print(type(tuple2))  #<class 'tuple'>
print(type(dict))  #<class 'dict'>
print(type(set))  #<class 'set'>


  #list 컴프리헨션로 초기화 & 출력
arr = [x for x in range(10)]
print(arr)

  #list 슬라이싱
print(list[:3])
print(list[1:])
 

  #반복문 흐름 따라가기
n, m = map(int, input().split())
for i in range(n, m, 1):
  for j in range(i + m, i, -1):
    print(i, j)


  #조건문 if, elif


  #각종 연산자 / ++, -- 불가능, +=, -= 가능
print(5 / 2)  #나머지까지
print(5 // 2)  #목만
print(5 % 2)  #나머지만


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


  #list 역출력
a_reverse =''
a = input()
  #첫번째 방법
print(a[::-1])

  #두번째 방법
for i in a:
  a_reverse = i + a_reverse
print(a_reverse)