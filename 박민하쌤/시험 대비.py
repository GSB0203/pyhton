list = [10, 20, 30, 40]
tuple = (10, 20)
dict = {1:10}
set = {20}
bool = True

print(type(bool))
print(type(list))
print(type(tuple))
print(type(dict))
print(type(set))


print(list[:3])
print(list[1:])

a_reverse =''
a = input()
for i in a:
  a_reverse = i + a_reverse
print(a_reverse)