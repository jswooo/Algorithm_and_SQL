def solution(p):
    p.sort()
    for i in range(0,len(p)-1):
        if p[i] == p[i+1][:len(p[i])]:
            return False
    return True