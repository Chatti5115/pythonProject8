import sys
from collections import deque

count = 0
n = int(input())
list = list(sys.stdin.readline())


def solution(count):
    first_node = list[0]
    if first_node == '(':
        count += 1
    elif first_node == ')':
        count -= 1
    list.popleft()
    if count is 0:
        print("YES")
    else:
        print("NO")

for _ in range(n):
    solution(list)


