def solution(nums):
    p = len(nums)//2 
    diff = len(set(nums))
    if (p < diff):
        return p 
    else:
        return diff