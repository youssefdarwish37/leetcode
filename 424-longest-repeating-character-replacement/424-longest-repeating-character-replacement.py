class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dict={}
        res=0
        l=0
        for r in range(len(s)):
            dict[s[r]]=1+dict.get(s[r],0)
            if (r-l+1)-max(dict.values())>k:
                dict[s[l]]-=1
                l+=1
            res=max(res,r-l+1)
        return res
            
        