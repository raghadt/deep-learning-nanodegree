import numpy as np

# Write a function that takes as input a list of numbers, and returns
# the list of values given by the softmax function.
def softmax(L):
    expoList = np.exp(L);
    sume = sum(expoList);
    result = [];
    for i in expoList:
        r = i*1.0/sume;
        result.append(r);

    return result;
