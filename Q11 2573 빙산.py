import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
T = []
que = deque()
for i in range(n) : 
    T.append(list(map(int, input().split())) + [None])
    for j in range(m) : 
        if T[i][j] != 0 : 
            que.append([i, j])
T.append([None for i in range(m + 1)])

que.append(['year', None])

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def cutcheck(ice) : 
    foot = {}
    for a, b in ice : 
        foot[(a, b)] = True
    a, b = ice[0][0], ice[0][1]
    foot[(a, b)] = False
    q = deque()
    q.append([a, b])
    check = 1
    while q : 
        a, b = q.popleft()
        for i in range(4) : 
            x = a + dx[i]
            y = b + dy[i]
            if [x, y] in ice and foot[(x, y)] : 
                foot[(x, y)] = False
                q.append([x, y])
                check = check + 1
    if check != len(ice) : 
        return True
    return False


year = -1
while que : 
    a, b = que.popleft()
    if a != 'year' : 
        count = 0
        for i in range(4) : 
            x = a + dx[i]
            y = b + dy[i]
            if year < T[x][y] <= 0 : 
                count = count + 1
        if T[a][b] > count : 
            que.append([a, b])
            T[a][b] = T[a][b] - count
        else : 
            T[a][b] = year
    else : 
        if len(que) == 0 : 
            print(0)
            exit(0)
        else : 
            if cutcheck(que) : 
                print(-year)
                exit(0)
            else : 
                year = year - 1
                que.append(['year', None])
