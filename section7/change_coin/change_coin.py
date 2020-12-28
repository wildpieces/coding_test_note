import sys
sys.stdin = open("section7/change_coin/in5.txt", "rt")

def DFS(L, total):
  global cnt
  if total > T:
    return
  if L == k:
    if total == T:
      cnt += 1
  else:
      for i in range(n[L]+1):
        DFS(L+1, total + p[L] * i)

if __name__ == "__main__":
  T = int(input())
  k = int(input())
  p = list()
  n = list()
  for _ in range(k):
    a, b = map(int, input().split())
    p.append(a)
    n.append(b)
  cnt = 0
  DFS(0, 0)
  print(cnt)

    