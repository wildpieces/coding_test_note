import sys
sys.stdin = open("section3/hourglass/in5.txt", "rt")

n = int(input())
mat = [list(map(int, input().split())) for _ in range(n)]
m = int(input())

for i in range(m):
  n_row, direction, move = map(int, input().split())
  if direction == 0:
    for _ in range(move):
      mat[n_row - 1].append(mat[n_row-1].pop(0))
  else:
    for _ in range(move):
      mat[n_row - 1].insert(0, mat[n_row-1].pop())

gam = 0
for j in range(n//2 + 1):
  if j == n//2:
    gam_row = mat[j][j]
  else:
    a = sum(mat[j][j:n-j])
    b = sum(mat[-1-j][j:n-j])
    gam_row = a + b
  gam += gam_row
print(gam)