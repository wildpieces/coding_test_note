import sys
sys.stdin = open("section4/wrestler_greedy/in5.txt", "rt")

n = int(input())
info = [tuple(map(int, input().split())) for _ in range(n)]
info.sort(key = lambda x : x[0], reverse = True)

cnt = 0
largest = -2147000000
for h, w in info:
  if w > largest:
    largest = w
    cnt += 1
print(cnt)
  

