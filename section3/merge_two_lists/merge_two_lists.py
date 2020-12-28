import sys
sys.stdin = open("section3/merge_two_lists/in1.txt", "rt")

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

p1 = p2 = 0
combine_list = []
while p1 < n and p2 < m:
  if a[p1] <= b[p2]:
    combine_list.append(a[p1])
    p1 += 1
  else:
    combine_list.append(b[p2])
    p2 += 1
if p1 < n:
  combine_list = combine_list + a[p1:]
if p2 < m:
  combine_list = combine_list + b[p2:]

for x in combine_list:
  print(x, end = ' ')
# combine_list = []
# for _ in range(2):
#   n = map(int, input())
#   lst1 = list(map(int, input().split()))
#   combine_list = combine_list + lst1

# combine_list.sort()
# for x in combine_list:
#   print(x, end = " ")

