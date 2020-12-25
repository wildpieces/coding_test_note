import sys
sys.stdin = open("section7/vacation_dfs/in5.txt", "rt")

def DFS(L, sum):
  global total_pay
  if L == n+1:
    if sum > total_pay:
      total_pay = sum
  else:
    if L + days[L] < n+1:
      DFS(L+days[L], sum + pay[L])
    DFS(L+1, sum)


if __name__ == "__main__":
  n = int(input())
  days = list()
  pay = list()
  for i in range(n):
    t, p = map(int, input().split())
    days.append(t)
    pay.append(p)
  total_pay = -2147000000
  days.insert(0, 0)
  pay.insert(0, 0)
  DFS(1, 0)
  print(total_pay)
