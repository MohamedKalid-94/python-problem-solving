# Phase 15 - Interview-Level Python
# 11 Coding Patterns

def counter_pattern(nums):
    count=0
    for n in nums: count+=n
    return count

def frequency_pattern(nums):
    result={}
    for n in nums: result[n]=result.get(n,0)+1
    return result

def two_pointer(nums,target):
    left,right=0,len(nums)-1
    while left<right:
        total=nums[left]+nums[right]
        if total==target:return [left,right]
        if total<target:left+=1
        else:right-=1
    return []

def sliding_window(nums,k):
    return max(sum(nums[i:i+k]) for i in range(len(nums)-k+1))

def main():
    print("Counter:",counter_pattern([1,2,3]))
    print("Frequency:",frequency_pattern([1,1,2]))
    print("Two Pointer:",two_pointer([1,2,3,4],5))
    print("Sliding Window:",sliding_window([1,2,3,4,5],3))

if __name__=="__main__": main()