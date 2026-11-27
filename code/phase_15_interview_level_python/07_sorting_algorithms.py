# Phase 15 - Interview-Level Python
# 07 Sorting Algorithms

def bubble_sort(nums):
    for i in range(len(nums)):
        for j in range(len(nums)-1):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
    return nums

def selection_sort(nums):
    for i in range(len(nums)):
        m=i
        for j in range(i+1,len(nums)):
            if nums[j]<nums[m]: m=j
        nums[i],nums[m]=nums[m],nums[i]
    return nums

def main():
    nums=[5,2,8,1]

    print("Bubble:",bubble_sort(nums.copy()))
    print("Selection:",selection_sort(nums.copy()))

if __name__=="__main__": main()