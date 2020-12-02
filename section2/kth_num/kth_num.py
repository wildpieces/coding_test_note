import sys
sys.stdin = open("section2/kth_num/in5.txt", "rt")

# how to work stdin, input, readline
# how to work open function and possible options
T = int(input())
for t in range(T):
  n, s, e, k = map(int, input().split())
  a = list(map(int, input().split()))
  b = a[s-1:e]
  b.sort()
  print("#%d %d" %(t+1, b[k-1]))