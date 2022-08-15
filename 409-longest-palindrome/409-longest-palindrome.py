class Solution:
    def longestPalindrome(self, s: str) -> int:
        dict={}
        result=0 
        odd_values=0
        for char in s:
            if char not in dict:
                dict[char]=1
            else:
                dict[char]+=1
        if len(dict)==1:
            return dict[s[0]]
        for i in dict.values():
            if i>1:
                if i%2==0:
                    result+=i
                else:
                    result += i -1
                    odd_values += 1
            else:
                odd_values+=1
        if odd_values>0:
            result+=1
        return result
            