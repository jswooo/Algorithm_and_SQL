def solution(array, commands):
    ans = []
    
    for x, y, z in commands:
        temp = sorted(array[(x-1):y])
        ans.append(temp[z-1])
    
    return ans