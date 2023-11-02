s = 'a b c d e'
s_re = ''
for i in range(len(s)-1, -1, -1):
  print(s[i], end='')

print()

for char in s:
  s_re = char + s_re
print(s_re)

print(s[::-1])
