import sys
sys.stdin = open("section3/circular_string_test/in5.txt", "rt")

n = int(input())

# for i in range(n):
#   string = input()
#   string = string.upper()
#   size = len(string)
#   for j in range(size // 2):
#     if string[j] != string[-j-1]:
#       print("#%d NO" %(i+1))
#       break
#   else:
#     print("#%d YES" %(i+1))

for i in range(n):
  string = input()
  string = string.upper()
  if string == string[::-1]:
    print("#%d YES" %(i+1))
  else:
    print("#%d NO" %(i+1))
  
