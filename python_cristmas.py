''' 
n = 1 width = 7
n = 2 width = 9
n = 3 width = 11
n = 4 width = 13
n = 5 width = 15
'''
n = int(input())
width = 7+((2*n)-2)
start = 1
stop = 8
for i in range(n):
  for j in range(start, stop, 2):  #7
    a='*'*j
    print(a.center(width))
  start += 2
  stop += 2
for i in range(3):
  base = '*'*3
  print(base.center(width))