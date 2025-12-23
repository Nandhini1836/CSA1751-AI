from collections import deque

goal = [[1,2,3],[4,5,6],[7,8,0]]

def bfs(start):
    q = deque([(start, [])])
    visited = set()

    while q:
        state, path = q.popleft()
        if state == goal:
            return path

        visited.add(tuple(map(tuple, state)))

        x, y = [(i,j) for i in range(3) for j in range(3) if state[i][j]==0][0]
        moves = [(0,1),(1,0),(0,-1),(-1,0)]

        for dx,dy in moves:
            nx, ny = x+dx, y+dy
            if 0<=nx<3 and 0<=ny<3:
                new = [row[:] for row in state]
                new[x][y], new[nx][ny] = new[nx][ny], new[x][y]
                if tuple(map(tuple,new)) not in visited:
                    q.append((new, path+[new]))

start = [[1,2,3],[4,0,6],[7,5,8]]
print("Solution steps:", bfs(start))
