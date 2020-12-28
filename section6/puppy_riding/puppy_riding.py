import sys
sys.stdin = open("section6/puppy_riding/in5.txt", "rt")

def DFS(L, tot_sum, r_sum):
  global largest
  if tot_sum + (total - r_sum) < largest:
    return
  if tot_sum > c:
    return
  if L == n:
    if tot_sum > largest:
      largest = tot_sum
  else:
      DFS(L+1, tot_sum+ws[L], r_sum+ws[L])
      DFS(L+1, tot_sum, r_sum+ws[L])

if __name__ == "__main__":
  c, n = map(int, input().split())
  ws = [int(input()) for _ in range(n)]
  largest = -2147000000
  total = sum(ws)
  DFS(0, 0, 0)
  print(largest)

