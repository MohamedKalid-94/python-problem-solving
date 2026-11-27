# Phase 15 - Interview-Level Python
# 02 List Problems

def find_max(nums): return max(nums)

def find_min(nums): return min(nums)

def remove_duplicates(nums): return list(set(nums))

def reverse_list(nums): return nums[::-1]

def rotate_list(nums,k): return nums[-k:]+nums[:-k]

def move_zeros(nums): return [x for x in nums if x!=0]+[0]*nums.count(0)

def two_sum(nums,target):
    seen={}
    for i,n in enumerate(nums):
        if target-n in seen: return [seen[target-n],i]
        seen[n]=i
    return []

def main():
    nums=[1,2,3,4,0,2]

    print("Max:",find_max(nums))
    print("Min:",find_min(nums))
    print("Remove Duplicates:",remove_duplicates(nums))
    print("Reverse:",reverse_list(nums))
    print("Rotate:",rotate_list(nums,2))
    print("Move Zeros:",move_zeros(nums))
    print("Two Sum:",two_sum([2,7,11,15],9))

if __name__=="__main__": main()