import sys
sys.stdin = open("section2/reg_polyhedron/in5.txt", "rt")

n, m = map(int, input().split())

cnt = [0] * (n+m+1)
max_val = -2147000000
for i in range(1, n+1):
  for j in range(1, m+1):
    cnt[i+j] += 1
for i in range(n+m+1):
  if cnt[i] > max_val:
    max_val = cnt[i]
for i in range(n+m+1):
  if cnt[i] == max_val:
    print(i, end=' ')