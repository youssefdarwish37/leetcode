class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # index=0
        # for i in nums:
        #     if i == target:
        #         return (index)
        #         break
        #     index+=1
        # else:
        #     return -1
#         my solution was o(n)
# lets solve another one in o(logn)
        left_index=0
        right_index=len(nums)-1
        
        while(left_index<=right_index):
            mid=int((left_index+right_index)/2)
            if nums[mid]>target:
                right_index=mid - 1
            elif nums[mid]<target:
                left_index=mid+1
            else:
                return mid
        return -1
            
        