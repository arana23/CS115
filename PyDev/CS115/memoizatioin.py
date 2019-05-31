import time
from test.badsyntax_future3 import result
def fib(n):
    if n<=1:
        return n
    return fib(n-1)+fib(n-2)
start_time=time.time()
#print(fib(40))
#print('computation time without memization: :5.2f' % (time.time()* start_time))
# if key is in the dictionary, return the values associated with the key 
# do work
# use recursion to do the works, but store the results in a local variable
# store the result in the dictionary and return the result
def fib_memo(n):
    def fib_helper(n, memo):
        if n in memo:
            return memo[n]
        if n<=1:
            result=n
        else:
            result= fib_helper(n-1,memo)+fib_helper(n-2, memo)
        memo[n]=result
        return result
    return fib_helper(n, {})

start_time=time.time()
print(fib_memo(40))
print('Computation time with memoziation %.2f' % (time.time()-start_time))


def LCS(s1, s2):
    """returns the length of the longest common subsequence in string s1 & s2"""
    if s1== '' or s2== '':
        return 0
    # checks of the first position of the two variables are equal 
    if s1[0]==s2[0]:
        return 1+LCS(s1[1:], s2[1:])
    return max(LCS(s1,s2[1:]), LCS(s1[1:],s2)

#DO THIS
#def LCS_memo(s1,s2):
    #if s1 in s2
        #return s1[s2]              

# def fast_LCS(s1,s2):
#     def fast_LCS_helper(s1, s2,memo):
#         if (s1,s2) in memo:
#             return memo[(s1, s2)]
#         if s1=='' or s2=='':
#             result =0
#         elif s1[0]==s2[0]:
#             result =1 +fast_LCS_helper(s1[1:],s2[1:],memo)
#         else:
#             result = max(fast_LCS_helper(s1[1:], s2[1:],memo), fast_LCS_helper(s1[1:], s2, memo))

# def fast_LCS_with_vals(s1,s2):
#     def fast_LCS_helper(s1, s2,memo):
#         if (s1,s2) in memo:
#             return memo[(s1, s2)]
#         if s1=='' or s2=='':
#             result =[0,'']
#         elif s1[0]==s2[0]:
#             lose_both=fast_LCS_helper(s1[1:],s2[1:],memo)
#             result =[1+lose_both[0],s1[0]+lose_both[1]]
#         else:
#             useS1=fast_LCS_helper(s1, s2[1:],memo)
#             uses2=fast_LCS_helper(s1[1:],s2,memo)
#             if useS1[0]>useS2[0]:
#                 result=useS1
#             else:
#                 result=useS2
#             memo[(s1,s2)]=result
#             return result
#         return fast_LCS_helper(s1,s2,{})
#     
# def subset(target, lst):
#     ''' determines whether or not to create target sum using the values in the list can be 
#     be positive, negative, or zero '''
#     def subset_helper(target,current,memo):
#         if(target,current) in memo:
#             return memo[(target,current)]
#         if target==0
#             result= True
#         elif current> last:
#             result=False
#         else:
#             result=subset(target-lst[0], lst[1:])
#             uselst=subset(target, lst[1:])
#         if(usetar or uselst)
#             return True
#     
#     start_time=time.time()
#     print(fast_LCS_with_values("kajdflksdjlsdfjl","ksdfjhdsjkjdfh"))

print(LCS("ACT","AT"))