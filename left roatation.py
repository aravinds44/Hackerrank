n,d=map(int,input().split())

arr = list(map(int,input().split()))

arr2 = [0]*n

for i in range(n):
  arr2[(i-d)%n]=arr[i]

print(*arr2)
