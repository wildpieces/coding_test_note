import sys
sys.stdin = open("section7/two_arms_scales/in3.txt", "rt")

def DFS(L, weight):
  global res
  if L == n:
    if 0 < weight <= total:
      res.add(weight)
  else:
    DFS(L+1, weight + nums[L])
    DFS(L+1, weight - nums[L])
    DFS(L+1, weight)


if __name__ == "__main__":
  n = int(input())
  nums = list(map(int, input().split()))
  total = sum(nums)
  res = set()
  DFS(0, 0)
  print(total - len(res))