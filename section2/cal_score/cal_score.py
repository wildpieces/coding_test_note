import sys
sys.stdin = open("section2/cal_score/in5.txt", "rt")

n = int(input())
ox = list(map(int, input().split()))

score = 0
weight = 0
for x in ox:
  if x == 1:
    weight += 1
    score += weight
  else:
    weight = 0
print(score)