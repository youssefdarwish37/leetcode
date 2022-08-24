class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l=0
        res=[]
        for i in range(len(nums)):
            for r in range(l+1,len(nums)):
                if (nums[l]+nums[r])==target:
                    res.append(l)
                    res.append(r)
                    break
            l+=1
        return res
        