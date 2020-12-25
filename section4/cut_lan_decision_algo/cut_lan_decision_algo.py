import sys
sys.stdin = open("section4/cut_lan_decision_algo/in5.txt", "r")

k, n = map(int, input().split())
Line = []
res = 0
largest = 0
for i in range(k):
  tmp = int(input())
  Line.append(tmp)
  largest = max(largest, tmp)

def Count(len):
  cnt = 0
  for x in Line:
    cnt += (x // len)
  return cnt


lt = 1
rt = largest
while lt < rt:
  mid = (lt + rt) // 2
  if Count(mid) >= n:
    res = mid
    lt = mid + 1
  else:
    rt = mid - 1
print(res)