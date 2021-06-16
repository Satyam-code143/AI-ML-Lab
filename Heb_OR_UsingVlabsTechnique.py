import numpy as np

inputs=[np.matrix([-1,-1,1]),np.matrix([-1,1,1]),np.matrix([1,-1,1]),np.matrix([1,1,1])]
weights=np.matrix([[0.5,0.5,0.1]])
lr=0.4

act_fn=lambda x:2/(1+np.exp(-x))-1

def heb_learn():
    global weights
    for ip in inputs:
        weighted_sum=weights.dot(ip.T)
        op=np.round(act_fn(weighted_sum),4)
        weights=np.round(weights+lr*op.dot(ip),4)

print("OR gate using Hebbian Learning Rule:")
print("Initial weight matrix:")
print(weights)
print("Now learning")
heb_learn()
print("Learning complete")
print("New weight matrix:")
print(weights)

print("Testing:")
print("Inputs\tOutput")

for ip in inputs:
    weighted_sum=weights.dot(ip.T)
    op=np.round(act_fn(weighted_sum),4)
    xlist=ip.tolist()
    print(xlist[0][0],xlist[0][1],'\t',-1 if op<0 else 1)
    










            

