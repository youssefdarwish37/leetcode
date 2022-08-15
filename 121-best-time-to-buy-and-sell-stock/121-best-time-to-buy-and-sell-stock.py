class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini=0
        maxi=1
        prof=0
        for maxi in range(len(prices)):
            if prices[mini]<prices[maxi]:
                mp=(prices[maxi]-prices[mini])
                prof=max(prof,mp)
            else: 
                mini=maxi
            maxi+=1
        return prof
                
            

        