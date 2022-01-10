from sys import stdin, stdout

round = lambda x: (x+0.5)//1
k = int(stdin.readline())
x = 0
y = 0

for i in [int(i) for i in stdin.readline().split()]:
    if i == 0:
        x = x*2
        y+=1
    elif i == 1:
        x = x*2+1
        y+=1
    elif i == 2:
        if not x % 2:
            x /= 2 
        else:
            x = (x-1)/2
        y-=1
    elif i == 3:
        x -= 1
    elif i == 4:
        x += 1
stdout.write(f"{int(y)}\n{bin(int(x))[2:]}")