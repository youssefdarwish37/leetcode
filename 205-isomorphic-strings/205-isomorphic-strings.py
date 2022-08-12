class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hashmapst,hashmapts={},{}
        if len(s) == len(t):
            for i in range(len(s)):
                c1=s[i]
                c2=t[i]
                if((c1 in hashmapst and hashmapst[c1] != c2 )or(c2 in hashmapts and hashmapts[c2] != c1 )):
                     return False
                hashmapst[c1]=c2
                hashmapts[c2]=c1
            return True
        else :
            return False
        