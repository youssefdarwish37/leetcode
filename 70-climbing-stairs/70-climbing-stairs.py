class Solution:
    def climbStairs(self, n: int) -> int:
        #var1 is the before last
        #var2 is the last element both always have only one step
        var1=1
        var2=1
        for i in range(n-1):
            temp = var1
            var1=var1+var2
            var2=temp
        return var1
        