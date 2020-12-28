import sys
from collections import deque
sys.stdin = open("section5/save_princess_que/in5.txt", "r")

n, k = map(int, input().split())
deck = list(range(1, n+1))
deck = deque(deck)
while deck:
  for i in range(k-1):
    a = deck.popleft()
    deck.append(a)
  deck.popleft()
  if len(deck) == 1:
    print(deck[0])
    deck.popleft()