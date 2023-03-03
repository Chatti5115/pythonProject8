import sys
from collections import deque

x = sys.stdin.readline
n = int(x())
data_deque = deque()

def push_front(data):
    data_deque.appendleft(data)
def push_back(data):
    data_deque.append(data)
def pop_front():
    if not data_deque:
        print(-1)
    else:
        print(data_deque[0])
        data_deque.popleft()

def pop_back():
    if not data_deque:
        print(-1)
    else:
        print(data_deque[-1])
        data_deque.pop()

def size():
    print(len(data_deque))

def empty():
    if not data_deque:
        print(1)
    else:
        print(0)

def front():
    if not data_deque:
        print(-1)
    else:
        print(data_deque[0])

def back():
    if not data_deque:
        print(-1)
    else:
        print(data_deque[-1])

for _ in range(n):
    command = sys.stdin.readline().split()
    if command[0] == 'push_back':
        push_back(command[1])
    elif command[0] == 'push_front':
        push_front(command[1])
    elif command[0] == 'pop_front':
        pop_front()
    elif command[0] == 'pop_back':
        pop_back()
    elif command[0] == 'size':
        size()
    elif command[0] == 'empty':
        empty()
    elif command[0] == 'front':
        front()
    elif command[0] == 'back':
        back()