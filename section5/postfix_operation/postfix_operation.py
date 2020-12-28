import sys
sys.stdin = open("section5/postfix_operation/in5.txt", "rt")

s = input()
stack = []
res = 0
for x in s:
  if x.isdecimal():
    stack.append(int(x))
  else:
    a = stack.pop()
    b = stack.pop()
    if x == "+":
      stack.append(a + b)
    elif x == "-":
      stack.append(b - a)
    elif x == "*":
      stack.append(a * b)
    elif x == "/":
      stack.append(b / a)
print(stack[0])

