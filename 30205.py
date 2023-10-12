import sys
input = sys.stdin.readline

def solve(N, M, P):
    arr = [sorted([n for n in map(int, input().split()) if n != -1]) for _ in range(N)]
    for enemy in arr:
        item = M - len(enemy)
        for n in enemy:
            while item > 0 and P < n:
                item -= 1
                P *= 2
            if P >= n: P += n
            else: return 0
        P *= 2 ** item
    return 1

print(solve(*map(int,input().split())))
