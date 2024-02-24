import numpy as np

def calculate(list):
    if len(list)==9:    
        calculations={}
        l1=np.array(list)
        l1=l1.reshape(3,3)
        calculations["mean"]=[
            l1.mean(axis=0).tolist(),
            l1.mean(axis=1).tolist(),
            l1.mean().tolist()]
        calculations["variance"]=[
            l1.var(axis=0).tolist(),
            l1.var(axis=1).tolist(),
            l1.var().tolist()]
        calculations["standard deviation"]=[
            l1.std(axis=0).tolist(),
            l1.std(axis=1).tolist(),
            l1.std().tolist()]
        calculations["max"]=[
            l1.max(axis=0).tolist(),
            l1.max(axis=1).tolist(),
            l1.max().tolist()]
        calculations["min"]=[
            l1.min(axis=0).tolist(),
            l1.min(axis=1).tolist(),
            l1.min().tolist()]
        calculations["sum"]=[
            l1.sum(axis=0).tolist(),
            l1.sum(axis=1).tolist(),
            l1.sum().tolist()]
    else:
        raise ValueError("List must contain nine numbers.")


    return calculations