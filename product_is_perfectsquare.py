n,m=map(int,input().split())
p=n*m
l=[0,1,4,9,16,25,36,49,64,81,100]
if p in l:
   print("yes")
else:
   print("no")
