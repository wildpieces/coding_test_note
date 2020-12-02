import sys
sys.stdin = open("section2/kth_divisor/in5.txt", "rt")

n, k = map(int, input().split())
print(n, k)

cnt = 0
for i in range(1, n+1):
  if n % i == 0:
    cnt += 1
  if cnt == k:
    print(i)
    break
else:
  print(-1)