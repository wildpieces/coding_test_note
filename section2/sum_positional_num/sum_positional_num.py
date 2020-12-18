import sys
sys.stdin = open("section2/sum_positional_num/in5.txt", "rt")

n = int(input())
ns = list(input().split())
# print()
sum_num = 0
for i in range(n):
  sep_num = [int(ltt) for ltt in ns[i]]
  sum_sep_num = sum(sep_num)
  if sum_sep_num > sum_num:
    sum_num = sum_sep_num
print(sum_num)  




