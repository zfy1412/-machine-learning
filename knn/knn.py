import numpy as np
import math
import random
import matplotlib.pyplot as plt
class zfy:
    def __init__(self,p,z):
        self.p=p
        self.z=z
def getkey(x):
    return x.p
def plen(p1,p2):
    p3=p2-p1
    p4=math.hypot(p3[0],p3[1])
    return p4
p=np.array([0,0])
yb=[zfy(p,0)]
yz=[zfy(p,0)]
def learn():
    print("样本总数")
    n=int(input())
    for i in range(1,n+1,1):
        x=float(input())
        y=float(input())
        z=int(input())
        if z==1 :
            marke='o'
        else :
            marke='^'
        plt.scatter(x, y, marker=marke,c='b')
        p=np.array([x,y])
        yb.append(zfy(p,z))
    print("录入完毕")
    for i in range(1,int(n*0.1)+1,1):
        rand=random.randint(1,len(yb)-1)
        yz.append(yb.pop(rand))
    cnt=[0] 
    all=[]
    for i in range(1,len(yz),1):
        data=[]
        for j in range(1,len(yb),1):
            data.append(zfy(plen(yb[j].p,yz[i].p),yb[j].z))
        data.sort(key=getkey)
        all.append(data)
    for k in range(1,len(yb),1):
        cnt.append(0)
    for k in range(1,len(yb),1):
        for i in range(1,len(yz),1):
            for j in range(0,k,1):
                if all[i-1][j].z==yz[i].z :
                    cnt[k]=cnt[k]+1
    maxx=0
    k=0
    for i in range(1,len(yb),1):
        if cnt[i]>maxx:
            maxx=cnt[i]
            k=i
    return k
def main():
    k=learn()
    print("询问总数")
    n=int(input())
    print("种类数")
    kind=int(input())
    print("k是")
    print(k)
    for i in range(0,n,1):
        x=float(input())
        y=float(input())
        plt.scatter(x, y, marker='*',c='r')
        z=np.array([x,y])
        cs=[zfy(0,0)]
        cnt=[0]*(kind+1)
        for j in range(1,len(yb),1):
            cs.append(zfy(plen(yb[j].p,z),yb[j].z))
        cs.sort(key=getkey)
        for j in range(0,k,1):
            cnt[cs[j].z]=cnt[cs[j].z]+1
        maxx=0
        zz=0
        for i in range(1,kind+1,1):
            if cnt[i]>maxx:
                maxx=cnt[i]
                zz=i
        print("它是"+str(zz))
    plt.show()
if __name__ == "__main__":
    main()