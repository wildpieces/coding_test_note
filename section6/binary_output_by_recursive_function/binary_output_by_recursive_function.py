import sys
sys.stdin = open("section6/binary_output_by_recursive_function/in5.txt", "r")

def DFS(x):
  if x == 0:
    return
  else:
    DFS(x // 2)
    print(x % 2, end = ' ')


if __name__ == "__main__":
  n = int(input())
  DFS(n)

# blog post: how recursive function works in stack data structure