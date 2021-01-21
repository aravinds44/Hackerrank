n,q = input().split()
n=int(n)
q=int(q)
lastanswer = 0
arr=[]
for i in range(n):
    arr.append([])

for i in range(q):
    a,x,y = input().split()
    a = int(a)
    x = int(x)
    y=int(y)
    
    idx = (x^lastanswer)%n
    if a==1:
        arr[idx].append(y)
    elif a==2:
        size = len(arr[idx])
        lastanswer = arr[idx][y % size]
        print(lastanswer)

