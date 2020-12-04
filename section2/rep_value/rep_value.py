import sys
sys.stdin = open("section2/rep_value/in5.txt", "rt")

n = int(input())
scores = list(map(int, input().split()))
# round ->  round half even
# print(round(4.5)) -> 4
#a = 67.5
# a = a + 0.5
# int(a)
mu = round(sum(scores) / n, 1)

min_distance = 2147000000
for idx, x in enumerate(scores):
  distance = abs(x - mu)
  if distance < min_distance:
    min_distance = distance
    score = x
    std_idx = idx + 1
  elif distance == min_distance:
    if x > score:
      score = x
      std_idx = idx + 1
print(mu, std_idx)

