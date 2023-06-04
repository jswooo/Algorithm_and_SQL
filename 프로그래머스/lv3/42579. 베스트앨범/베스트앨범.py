def solution(g, p):
    d = dict()
    ans = []
    temp = [[g[i],p[i],i] for i in range(len(g))] # 장르, 재생횟수, idx를 리스트로 
    temp = sorted(temp, key = lambda x : (x[0], -x[1], x[2])) # 많이 재생될수록, 같다면 고유번호가 낮을수록 정렬 
    
    for i in temp:
        if i[0] not in d:
            d[i[0]] = i[1]
        else:
            d[i[0]] += i[1]
            
    d = sorted(d.items(), key = lambda x : -x[1]) # 전체 재생횟수가 높은 순서대로 정렬 
    
    for i in d:
        cnt = 0 
        for j in temp:
            if i[0] == j[0]:
                cnt += 1
                if cnt > 2:
                    break
                ans.append(j[2])
    
    return ans
                
    
    
        