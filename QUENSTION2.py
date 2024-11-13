import numpy as np
def longeststring(arr):
    longer_than5 = [s for s in arr if len(s)>5]
    if longer_than5:
        return max(longer_than5,key=len)
    
    return min(arr,key=len)

arr = np.array(["app","ba","kiw","mang","gu","chik"])
result = longeststring(arr)
print(result)
