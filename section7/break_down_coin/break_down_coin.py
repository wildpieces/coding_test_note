import sys
sys.stdin = open("section7/break_down_coin/in5.txt", "rt")
# RESOLVE THIS PROBLEM!!!!!


def DFS(L):
  global res
  if L == n:
    diff = max(money) - min(money)
    if res > diff:
      tmp = set()
      for x in money:
        tmp.add(x)
      if len(tmp) == 3:
        res = diff
  else:
    for i in range(3):
      money[i] += coins[L]
      DFS(L+1)
      money[i] -= coins[L]


if __name__ == "__main__":
  n = int(input())
  coins = [int(input()) for _ in range(n)]
  money = [0] * 3
  res = 2147000000
  DFS(0)
  print(res)