import sys
input = sys.stdin.readline


n= int(input().strip())
for i in range(n) :
    m1, m2, m3 = map(int,input().strip().split())
    g = [[0]*m1 for _ in range(m2)]
    v = [[0]*m1 for _ in range(m2)]
    for j in range(m3):
        a, b = map(int,input().strip().split())
        g[b][a] = 1
    print(g)


