n = int(input())

strings = [input() for i in range(n)]

q = int(input())


queries = [input() for i in range(q)]

for i in queries:
  print(strings.count(i))
