import sys
from collections import deque
sys.stdin = open("section5/emergency_room_que/in5.txt", "r")

# RESOLVE THIS !!!!!!!!!!!!!!!!
n, m = map(int, input().split())
Q = [(pos, val) for pos, val in enumerate(list(map(int, input().split())))]
Q = deque(Q)
cnt = 0
while True:
  a = Q.popleft()
  if any(a[1] < x[1] for x in Q):
    Q.append(a)
  else:
    cnt += 1
    if a[0] == m:
      break
print(cnt)


