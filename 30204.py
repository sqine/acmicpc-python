N, X = map(int,input().split())
s = sum(map(int, input().split()))
print(1 if s%X==0 else 0)