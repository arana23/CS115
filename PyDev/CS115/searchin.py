import random

def searchin(key, lst):
    count=0;
    for x in lst:
        count+=1
        if key==x:
            return count
    return -1

#if list is already sorted
""" lst - sort list, key - val to sort for
returns the index of key in lst or -low-1 if the key is not present the caller of this can convert index to a postive ind"""
def binary_search(lst, key):
    low=0
    high=len(lst)-1
    while high>=low:
        mid =low+(high-low)//2
        if key<lst(mid):
            high=mid-1
        elif key>lst(mid):
            low=mid+1
        else:
            return mid
    return -low-1

def mean(lst):
    tot=0
    for x in lst:
        tot+=x
    return tot/len(lst)

print(mean([1,2,3,4]))

def swap(lst, a, b):
    """swaps lst a with lst b"""
    temp= lst[a]
    lst[a]=lst[b]
    lst[b]=temp
    
def selectionsort(lst):
    n=len(lst)
    for i in range(n-1):
        min_ind=i
        for j in range(i+1,n):
            if lst[j]<lst[min_ind]:
                min_ind=j
        if min_ind!=i:
            swap(lst,i,min_ind)

random_list=[random.randint(1,10000)for _ in range(200000)]
copy_list=list(random_list)