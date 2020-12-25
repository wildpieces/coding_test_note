import sys
sys.stdin = open("section4/binary_search/in5.txt", "rt")

n, m = map(int, input().split())
a = list(map(int, input().split()))

lt = 0
rt = n - 1

while lt <= rt:
  mid = (lt + rt) // 2
  if a[mid] == m:
    break
  elif a[mid] > m:
    rt = mid - 1
  else:
    lt = mid + 1
print(mid)