import sys
sys.stdin = open("section2/kth_big_num/in5.txt", "rt")

n, k = map(int, input().split())
a = list(map(int, input().split()))
res = set()
for i in range(n):
  for j in range(i+1):
    for m in range(j+1):
      res.add(a[i]+a[j]+a[m])
res = list(res)
res.sort(reverse = True)
print(res[k-1])