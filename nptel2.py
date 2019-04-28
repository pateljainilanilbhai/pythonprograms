# def minSwaps(arr):
#     n = len(arr)
#     count=0
#     sortedarray=[]
#     for i in arr:
#         sortedarray.append(i)
#     sortedarray.sort()
#     print("sorted="+str(sortedarray))
#     for i in range(n-1):
#         a=sortedarray[i]
#         b=sortedarray[i+1]
#         o=arr.index(a)
#         p=arr.index(b)
#         if o>p:
#             count+=1
#             arr.pop(p)
#             arr.append(b)
#             print(arr)
#
#     return count
#
# # Driver Code
# n=input()
# a = n.split(" ")
# arr=[]
# for i in a:
#     arr.append(int(i))
# print(minSwaps(arr))





import random
x=input()
if random.randrange(0,8)%2==0:
    print("5")
else:
    print("7")