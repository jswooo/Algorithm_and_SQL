def solution(c):
    d = dict()
    s = set()
    ans = 1 
    
    for i in c:
        if i[1] not in s:
            d[i[1]] = 1
        else:
            d[i[1]] += 1 
        s.add(i[1])
    
    for i in s:
        ans *= (d[i]+1)
        
    return (ans-1)