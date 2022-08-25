class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s=list(s)
        i,j=0,0
        
        for i in range(len(s)):
            if s[j]=="#" and (j-1) > -1:
                s.pop(j)
                s.pop((j-1))
                j=j-2
            elif s[j]=="#":
                s.pop(j)
                j=j-1
            
            j+=1
        
        t=list(t)
        i,j=0,0
        
        for i in range(len(t)):
            if t[j]=="#"  and (j-1) > -1:
                t.pop(j)
                t.pop((j-1)) 
                j=j-2
            elif t[j]=="#":
                t.pop(j)
                j=j-1
            j+=1
            print(s,t)
        
        if s==t:
            return True
        else:
            return False