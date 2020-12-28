import sys
sys.stdin = open("section6/finding_subset/in1.txt", "rt")


def DFS(node):
  if node == n+1:
    for i in range(1, n+1):
      if check[i] == 1:
        print(i, end = '')
    print()
  else:
    check[node] = 1
    DFS(node + 1)
    check[node] = 0
    DFS(node + 1)

if __name__ == "__main__":
  n = int(input())
  check = [0] * (n+1)
  DFS(1)
