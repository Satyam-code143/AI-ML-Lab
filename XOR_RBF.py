import numpy as np

ip=np.array([[0,0],[0,1],[1,0],[1,1]])
t1=np.array([0,1])
t2=np.array([1,0])
w1=-1
w2=1

print("Input pattern | \u03A6\u2081(x)\t | \u03A6\u2082(x)\t | \u2211wi\u03A6i(x)\t | Output")
print("-"*58)

for data in ip:
    phi1=np.exp(-np.sum(((data-t1)**2)))
    phi2=np.exp(-np.sum(((data-t2)**2)))
    X=np.abs(w1*phi1+w2*phi2)
    output=1 if X>0 else 0
    print(data,'\t\t',np.round(phi1,4),'   ',np.round(phi2,4),'\t',np.round(X,4),'    ',output)
    
    
