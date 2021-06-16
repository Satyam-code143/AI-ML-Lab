import numpy as np

inputs=[np.matrix([-1,-1,1]),np.matrix([-1,1,1]),np.matrix([1,-1,1]),np.matrix([1,1,1])]
weights=np.matrix([[0.5,0.5,0.1]])
exp_op=[np.matrix([0]),np.matrix([1]),np.matrix([1]),np.matrix([1])]
lr=0.4

act_fn=lambda x:2/(1+np.exp(-x))-1

def cor_learn():
    global weights
    for i,ip in enumerate(inputs):
        weighted_sum=weights.dot(ip.T)
        op=np.round(act_fn(weighted_sum),4)
        weights=np.round(weights+lr*exp_op[i].dot(ip),4)

print("OR gate using Correlation Learning Rule:")
print("Initial weight matrix:")
print(weights)
print("Now learning")
cor_learn()
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
   










            

