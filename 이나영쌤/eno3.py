print("a","b")
print("나는 %d살이야" %20)
print("나는 %s좋아해요" %"파이썬")
print("나는 %s와%s색을 좋아해요" %("파란", "빨간"))
print("나는 {}살입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간"))


print("나는 {age}살과 {color}색을 좋아해요.".format(age=20, color="빨간"))
age=20
color="RED"
print(f"나는 {age}살이며, {color}을 좋아해요")


a=5
def func ():
  global a
  a=3
  return a

print(func())
print(a)

def profile(name, age=17, language="py"):
  print("이름 : {0}\t나이 : {1}\t 주사용언어 : {2}".format(name, age, language))

#profile("이나영", 20, "파이썬")
profile("이나영")


def func(*a):
  print(type(a))
  return print(sum(a))

func(1, 2, 3, 4, 5, 6)