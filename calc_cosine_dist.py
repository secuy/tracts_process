import numpy as np

# 假设a和b都是行向量
def calcCosDist(a, b):
    return (np.dot(a, b.T) / (np.sqrt((a*a).sum()) * np.sqrt((b*b).sum())))