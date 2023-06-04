def solution(my_string, overwrite_string, s):
    ans = ''
    ans += my_string[:s]
    ans += overwrite_string 
    ans += my_string[(len(overwrite_string) + s):]
    
    return ans