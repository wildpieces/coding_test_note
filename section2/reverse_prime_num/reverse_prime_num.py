import sys
sys.stdin = open("section2/reverse_prime_num/in5.txt", "rt")

n = int(input())
ns = list(map(int, input().split()))

def reverse(x):
  res = 0
  while x > 0:
    quotien = x % 10
    res = res * 10 + quotien
    x = x // 10
  return res

def isPrime(x):
  if x == 1:
    return False
  for i in range(2, x // 2 + 1):
    if x % i == 0:
      return False
  else:
    return True

for i in ns:
  reverse_num = reverse(i)
  if isPrime(reverse_num):
    print(reverse_num, end = " ")



