import sys
sys.stdin = open("section4/assign_meetingroom_greedy/in1.txt", "rt")


# RESOLVE THIS PROBLEM

n = int(input())
meetings = []
for i in range(n):
  s, e = map(int, input().split())
  meetings.append((s, e))
meetings.sort(key = lambda x: (x[1], x[0]))
end_time = 0
cnt = 0
for s, e in meetings:
  if s >= end_time:
    end_time = e
    cnt += 1
print(cnt)
