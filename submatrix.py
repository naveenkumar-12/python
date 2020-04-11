a =[[7, 3],[5,10]]
b = [[5, 8, 1, 2],
     [3, 3, 3, 3],
    [6, 7, 3, 0], 
    [4, 5, 9, 1]] 
s=0
f=0
p=0
while(f==0):
    l=[]
    r=p
    for i in range(0,len(a)):
        t=b[r][s:len(a[0])+s]
        l.append(t)
        r=r+1
    if(a==l):
        f=1
        print("Found")
    else:
        if(len(a[0])+s<len(b[0])):
            s+=1
        elif(r<len(b)):
            s=0
            p=p+1
        else:
            f=1
            print("Not found")
