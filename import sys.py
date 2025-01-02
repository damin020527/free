import sys
input = sys.stdin.readline

z =[]
c=0
q = []
n= int(input().strip())
for i in range(n) :
    m1, m2, m3 = map(int,input().strip().split())
    g = [[0]*m1 for i in range(m2)]
    for j in range(m3):
        a, b = map(int,input().strip().split())
        g[b][a] = 1
    #print(g)

for k in range(m1) :
    for p in range(m2) :
        if g[k][p] == 1 and [k,p] not in z:
            z.append([k,p])
            q.append([k,p])
            c = c+1
        while len(q) != 0 :
            pp= q.pop(0)
            k = pp[0]
            p = pp[1]
            try :
                if g[k-1][p] == 1 and [k-1,p] not in z:
                    z.append([k-1,p])
                    q.append([k-1,p])
            except IndexError:
                pass

            try :    
                if g[k+1][p] == 1 and [k+1,p] not in z:
                    z.append([k+1,p])
                    q.append([k+1,p])
            except IndexError:
                pass
            try :
                if g[k][p-1] == 1 and [k,p-1] not in z:
                    z.append([k,p-1])
                    q.append([k,p-1])
            except IndexError:
                pass
            try :
                if g[k][p+1] == 1 and [k,p+1] not in z:
                    z.append([k,p+1])
                    q.append([k,p+1])
            except IndexError:
                pass
print(c)




