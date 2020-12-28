import sys
sys.stdin = open("section4/setting_up_stable/in5.txt", "r")

n, c = map(int, input().split())
line = []
for _ in range(n):
  l = int(input())
  line.append(l)
line.sort()

def nHorse(dist):
  n_horse = 1
  end_point = line[0]
  for i in range(1, n):
    if line[i] - end_point >= dist:
      n_horse += 1
      end_point = line[i]
  return n_horse


lt = 1
rt = max(line)
while lt <= rt:
  mid = (lt + rt) // 2
  if nHorse(mid) >= c:
    res = mid
    lt = mid + 1
  else:
    rt = mid - 1
print(res)