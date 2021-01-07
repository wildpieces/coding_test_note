import sys
sys.stdin = open("section3/apple_tree/in5.txt", "r")

n = int(input())
mat = [list(map(int, input().split())) for _ in range(n)]

recurr = n//2 
apple_sum = 0
for i in range(recurr+1):
  if i == recurr:
    n_apple = sum(mat[i])
  else:
    a = sum(mat[i][recurr-i:recurr+i+1])
    b = sum(mat[-1-i][recurr-i:recurr+i+1])
    n_apple = a + b
  apple_sum += n_apple
print(apple_sum)
# s = e = n//2
# for i in range(n):
#   for j in  range(s, e+1):
#     apple_sum += mat[i][j]
#   if i < n//2:
#     s -= 1
#     e += 1
#   else:
#     s += 1
#     e -= 1
# print(apple_sum)