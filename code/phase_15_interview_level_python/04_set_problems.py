# Phase 15 - Interview-Level Python
# 04 Set Problems

def remove_duplicates(nums): return set(nums)

def intersection(a,b): return set(a)&set(b)

def union(a,b): return set(a)|set(b)

def difference(a,b): return set(a)-set(b)

def is_subset(a,b): return set(a).issubset(set(b))

def main():
    a=[1,2,3,4]
    b=[3,4,5,6]

    print("Unique:",remove_duplicates(a))
    print("Intersection:",intersection(a,b))
    print("Union:",union(a,b))
    print("Difference:",difference(a,b))
    print("Subset:",is_subset([1,2],a))

if __name__=="__main__": main()