import sys
sys.stdin = open("section2/num_of_prime_num/in5.txt", "rt")

n = int(input())
ch = [0] * (n+1)
cnt = 0
for i in range(2, n+1):
  if ch[i] == 0:
    cnt += 1
    for j in range(i, n+1, i):
      ch[j] = 1
print("%d; # of prime number %d" %(n, cnt) )
