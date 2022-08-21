# class Solution:
#     import math
#     def uniquePaths(self, m: int, n: int) -> int:
         
#         return int(math.factorial(m+n-2)/(math.factorial(m-1)*math.factorial(n-1)))
class Solution:

     def uniquePaths(self, m: int, n: int) -> int:
            lastrow=[1]*n
            for i in range (m-1):
                newrow=[1]*n
                for j in range (n-2,-1,-1):
                    newrow[j]=newrow[j+1]+lastrow[j]
                lastrow =newrow
            return lastrow[0]
         
