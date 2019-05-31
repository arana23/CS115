'''
Created on Nov 9, 2018

@author: arana3
'''

def num_matches(list1, list2):
    list1.sort()
    list2.sort()
    matches = i = j = 0
    while i < len(list1) and j < len(list2):
        if(list1[i]==list2[j]):
            matches+=1
            i+=1
            j+=1
        elif list1[i]<list2[j]:
            i+=1
        else:
            j+=1
    return matches

A=[2, 3, 5, 7, 9, 11, 13, 17, 23]
B=[11, 13, 15, 17, 19, 21, 23, 25, 27]
matches=num_matches(A,B)
print(matches)

def keep_matches(list1, list2):
    matchlist=[]
    list1.sort()
    list2.sort()
    i = j = 0
    while i < len(list1) and j < len(list2):
        if(list1[i]==list2[j]):
            matchlist.append(list1[i])
            i+=1
            j+=1
        elif list1[i]<list2[j]:
            i+=1
        else:
            j+=1
    return matchlist

print(keep_matches(A, B))

def drop_matches(list1, list2):
    matchlist=[]
    list1.sort()
    list2.sort()
    i = j = 0
    while i < len(list1) and j < len(list2):
        if(list1[i]==list2[j]):
            i+=1
            j+=1
        elif list1[i]<list2[j]:
            i+=1
        else:
            matchlist.append(list1[j])
            j+=1
    while j < len(list2):
        matchlist.append(list2[j])
        j+=1
    return matchlist

print(drop_matches(A, B))