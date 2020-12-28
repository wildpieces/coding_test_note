import sys
sys.stdin = open("section3/maxsum_gridplate/in5.txt", "r")

n = int(input())
mat = [list(map(int, input().split())) for _ in range(n)]
largest = -2147000000
for i in range(n):
  sum1 = sum2 = 0
  for j in range(n):
    sum1 += mat[i][j]
    sum2 += mat[j][i]
  if sum1 > largest:
    largest = sum1
  if sum2 > largest:
    largest = sum2
sum1 = sum2 = 0
for i in range(n):
  sum1 += mat[i][i]
  sum2 += mat[i][n-i-1]
if sum1 > largest:
  largest = sum1
if sum2 > largest:
  largest = sum2
print(largest)