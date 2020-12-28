import sys
sys.stdin = open("section3/sum_numbers/in2.txt", "rt")

n, m = map(int, input().split())
nums = list(map(int, input().split()))
# cnt = 0
# for i in range(n):
#   k = 1
#   num_sum = nums[i]
#   while num_sum < m and (i+k) <= n-1:
#     num_sum += nums[i+k]
#     k += 1
#   if num_sum == m:
#     cnt += 1
# print(cnt)

lt = 0
rt = 1
cnt = 0
num_sum = nums[0]
while True:
  if num_sum < m:
    if rt < n:
      num_sum += nums[rt]
      rt += 1
    else:
      break
  elif num_sum == m:
    cnt += 1
    num_sum -= nums[lt]
    lt += 1
  else:
    num_sum -= nums[lt]
    lt += 1
print(cnt)