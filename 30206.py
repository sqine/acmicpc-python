import sys
input = sys.stdin.readline
MAX_NUMBER = 1_000_000_007

N, M = map(int, input().split())
routes = [[] for _ in range(N+1)]
visited = [False]*2 + [True]*N

for _ in range(M):
    a, b = map(int, input().split())
    routes[a].append(b)
    routes[b].append(a)

next, ans = [1], 2
while next:
    cur, next = next, []
    cnt = 0
    for fr in cur:
        for to in routes[fr]:
            if visited[to]:
                visited[to] = False
                next.append(to)
                cnt += 1
    ans = ans * (cnt+1) % MAX_NUMBER

print((ans-1)%MAX_NUMBER)
