from sys import stdin, stdout
m, start, a, b, length, k = map(int, stdin.readline().split())
lst = [int(str(start*a+b+(10**(m*4)))[m+1:-m])]
minv = 10**(m*3)
idxs = dict()
for i in range(length):
    t = int(str(lst[-1]*a+b+(10**(m*4)))[m+1:-m])
    lst.append(t)
    if t in idxs:
        if minv > i-idxs[t]:
            minv = i-idxs[t]
    else:
        idxs[t] = i
stdout.write(f"{minv}\n{sorted(lst)[-k]}")