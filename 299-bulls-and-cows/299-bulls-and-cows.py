class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bull,cow=0,0
        s=list(secret)
        g=list(guess)
        i,j=0,0
        for i in range(len(s)):
            if s[j]==g[j]:
                bull+=1
                s.pop(j)
                g.pop(j)
            else:
                j+=1
        count=Counter(s)
        for l in g:
            if l in count and count[l]>0:
                cow+=1
                count[l]-=1
        return str(bull) + "A" + str(cow) + "B"