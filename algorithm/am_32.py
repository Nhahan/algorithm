import sys

N, M, V = map(int, (sys.stdin.readline()).split())

points = [[]]
points2 = [[]]
for m in range(N):
    points.append([])
    points2.append([])
for m in range(1, M + 1):
    a, b = map(int, (sys.stdin.readline()).split())
    points[a].append(b)
    points2[a].append(b)
    points[b].append(a)
    points2[b].append(a)
    points[a].sort(reverse=True)
    points2[a].sort()
    points[b].sort(reverse=True)
    points2[b].sort()


def dfs(graph, start):
    stack = [start]
    visited = []
    while len(stack) != 0:
        cur_node = stack.pop()
        if cur_node not in visited:
            visited.append(cur_node)
        for node in graph[cur_node]:
            if node not in visited:
                stack.append(node)
    return visited


dfs_list = dfs(points, V)
for dfs in dfs_list:
    if dfs == dfs_list[-1]:
        print(dfs)
    else:
        print(dfs, "", end="")

def bfs(graph, start):
    queue = [start]
    visited = list()
    visited.append(start)
    while queue:
        cur_node = queue.pop(0)
        if cur_node not in visited:
            visited.append(cur_node)
        for node in graph[cur_node]:
            if node not in visited and node not in queue:
                queue.append(node)

    return visited


bfs_list = bfs(points2, V)

for bfs in bfs_list:
    if bfs == bfs_list[-1]:
        print(bfs)
    else:
        print(bfs, "", end="")
