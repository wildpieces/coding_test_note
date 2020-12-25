import sys
sys.stdin = open("section5/iron_bar_stack/in5.txt", "r")
s = input()

stack = []
cnt = 0
for i in range(len(s)):
  if s[i] == "(":
    stack.append(s[i])
  else:
    stack.pop()
    if s[-1] == "(":
      cnt += len(stack)
    else:
      cnt += 1
print(cnt)