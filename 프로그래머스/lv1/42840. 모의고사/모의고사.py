def solution(answers):
    s1, s2, s3 = 0, 0, 0
    ans = []
    num1 = [1,2,3,4,5]*2000
    num2 = [2, 1, 2, 3, 2, 4, 2, 5] * 1250
    num3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000
    
    for i in range(len(answers)):
        if answers[i] == num1[i]: 
            s1 += 1 
        if answers[i] == num2[i]:
            s2 += 1 
        if answers[i] == num3[i]:
            s3 += 1 
    
    m = max(s1, s2, s3)
    
    if m == s1:
        ans.append(1)
    if m == s2:
        ans.append(2)
    if m == s3:
        ans.append(3)
        
    return ans
    