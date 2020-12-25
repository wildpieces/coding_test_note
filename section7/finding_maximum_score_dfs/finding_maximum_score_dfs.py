import sys
sys.stdin = open("section7/finding_maximum_score_dfs/in5.txt", "rt")

def DFS(L, sum, time):
  global total_score
  if time > m:
    return
  if L == n:
    if sum > total_score:
      total_score = sum
  else: 
    DFS(L+1, sum + score[L], time + spend_time[L])
    DFS(L+1, sum, time)


if __name__ == "__main__":
  n, m = map(int, input().split())
  score = list()
  spend_time = list()
  total_score = -2147000000
  for i in range(n):
    s, t = map(int, input().split())
    score.append(s)
    spend_time.append(t)
  DFS(0, 0, 0)
  print(total_score)