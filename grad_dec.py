import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import inv


x=np.array([[1,11],[1,20],[1,32],[1,40],[1,50]])
y=np.array([[10],[22],[29],[41],[54]])
xt=np.transpose(x)
#q=np.dot(inv(np.dot(xt,x)),np.dot(xt,y))



def a_der(x,y,a,b):
    s=0
    for i in range(5):
        s=s-0.2*(y[i][0]-(a*x[i][1]+b))*x[i][1]
    return s
def b_der(x,y,a,b):
    s=0
    for i in range(5):

        s=s-0.2*(y[i][0]-(a*x[i][1]+b))
    return s
def bla(al,a,b,x,y):
    while(True):
        temp=a-al*a_der(x,y,a,b)
        temp1=b-al*b_der(x,y,a,b)
        a=temp
        b=temp1
        print(a)
        if abs(a_der(x,y,a,b))<0.0001 and abs(b_der(x,y,a,b))<0.0001:
            break
    return (a,b)
d=bla(0.001,1,1,x,y)
print(d)
plt.plot(x[:,1],y[:])
plt.plot(x[:,1],d[0]*x[:,1]+d[1])
plt.show()
