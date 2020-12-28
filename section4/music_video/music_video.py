import sys
sys.stdin = open("section4/music_video/in1.txt", "rt")
## RESOLVE THIS!!!

n, m = map(int, input().split())
s = list(map(int, input().split()))
largest = max(s)

def numDvd(capacity):
  nDvd = 1
  run_time = 0
  for x in s:
    if run_time + x > capacity:
      nDvd += 1
      run_time = x
    else:
      run_time += x
  return nDvd


lt = 1
rt = sum(s)
res = 0
while lt <= rt:
  mid = (lt + rt) // 2
  if mid >= largest and numDvd(mid) <= m:
    res = mid
    rt = mid - 1
  else: 
    lt = mid + 1
print(res)


