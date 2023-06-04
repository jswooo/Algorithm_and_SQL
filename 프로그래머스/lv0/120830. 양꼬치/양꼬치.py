def solution(n, k):
    service = n // 10 
    ans = 12000 * n 
    k -= service 
    if (k>=0):
        ans += 2000 * k 
    
    return ans