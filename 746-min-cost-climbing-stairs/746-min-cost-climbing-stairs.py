class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # cast=0
        # cost.append(0)
        # print (cost)
        # c=0
        # for i in range (0,len(cost)-1):
        #     if c>(len(cost)-2):
        #         break
        #     if cost[c]>=cost[c+1]:
        #         cast+=cost[c+1]
        #         c+=2
        #     else:
        #         cast+=cost[c]
        #         c+=1
        # return cast 
        #this work if the last array was the end and it is not dp
        cost.append(0)
        for i in range(len(cost)-3,-1,-1):
            cost[i]+=min(cost[i+1],cost[i+2])
        return min(cost[0],cost[1])