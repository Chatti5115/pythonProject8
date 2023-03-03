import sys
from collections import deque

x = sys.stdin.readline
n = int(x())
q_que = deque()


def push(data):
    q_que.append(data)

def pop():
    if not q_que:
        print(-1)
    else:
        print(q_que.popleft())
def size():
    print(len(q_que))

def empty():
    if not q_que:
        print(1)
    else:
        print(0)

def front():
    if not q_que:
        print(-1)
    else:
        print(q_que[0])
def back():
    if not q_que:
        print(-1)
    else:
        print(q_que[-1])


for _ in range(n):
    command = sys.stdin.readline().split()
    if command[0] == 'push':
        push(command[1])
    elif command[0] == 'pop':
        pop()
    elif command[0] == 'size':
        size()
    elif command[0] == 'empty':
        empty()
    elif command[0] == 'front':
        front()
    elif command[0] == 'back':
        back()
