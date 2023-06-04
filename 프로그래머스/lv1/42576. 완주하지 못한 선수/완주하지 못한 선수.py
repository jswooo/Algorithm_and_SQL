def solution(part, comp):
    hdict = dict()
    sum = 0 
    for i in part:
        hdict[hash(i)] = i 
        sum += hash(i)
    
    for i in comp:
        sum -= hash(i)
    
    return hdict[sum]