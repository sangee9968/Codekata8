s1=input()
idx=len(s1)//2
s2=list(s1)
s2[idx]='*'
s3=''.join(s2)
if len(s1)%2==0:
  s2[idx-1]='*'
  s3=''.join(s2)
  print(s3) 
else:
  s2[idx]='*'
  s3=''.join(s2)
  #print result
  print(s3)
