import sys
sys.stdin = open("section2/dice_rules/in5.txt", "rt")

n = int(input())
res = 0
for i in range(n):
  score = input().split()
  score.sort()
  a, b, c = map(int, score)
  if a == b and b == c:
    money = 10000 + a * 1000
  elif a == b or a == c:
    money = 10000 + a * 100
  elif b == c:
    money = 10000 + b * 100
  else:
    money = c * max(a, b, c)
  if money > res:
    res = money
print(res)