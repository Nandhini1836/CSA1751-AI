from collections import deque

def water_jug(j1, j2, target):
    visited = set()
    q = deque([(0,0)])

    while q:
        a,b = q.popleft()
        if (a,b) in visited:
            continue
        visited.add((a,b))

        if a == target or b == target:
            print("Reached:", a, b)
            return

        q.extend([
            (j1,b),(a,j2),(0,b),(a,0),
            (a-min(a,j2-b), b+min(a,j2-b)),
            (a+min(b,j1-a), b-min(b,j1-a))
        ])

water_jug(4,3,2)
