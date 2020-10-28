def drawDia(n):
  for i in range(n):
    for j in range(n-i-1, 0, -1):
      print(" ",end='')
    for k in range(0, 2*i+1):
      print("*",end='')
    print('\t')
  for i in range(1,n):
    for j in range(i):
      print(" ",end='')
    for k in range(1,2*n-2*i):
      print("*",end='')
    print('\t')


n = int(input())
drawDia(n)
