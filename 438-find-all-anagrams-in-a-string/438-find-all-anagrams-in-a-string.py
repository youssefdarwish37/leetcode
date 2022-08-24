class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pMap,sMap={},{}
        if len(p)>len(s):
            
            return []
        for k in range(len(p)):  
            pMap[p[k]]=1+pMap.get(p[k],0)
            sMap[s[k]]=1+sMap.get(s[k],0)
            
        if  pMap==sMap:
            res=[0]
        else:
            
            res=[]
        l=0
        for r in range(len(p),len(s)):
            sMap[s[r]]=1+sMap.get(s[r],0)
            sMap[s[l]]-=1
            if sMap[s[l]]==0:
                sMap.pop(s[l])
            l+=1
            if sMap==pMap:
                res.append(l)
        return res
            
            
#         if len(p)>len(s):
#             return []
#         l,r=0,(len(p)-1)
#         list=[]
#         for i in range(len(s)-(len(p))+1):
#             c=0
#             dict={}
#             for k in range(l,r+1):  
#                 if s[k] in dict:
#                     dict[s[k]]=dict[s[k]]+1
#                 else:
#                     dict[s[k]]=1
#             for j in range(len(p)):
#                 if p[j] in dict :
#                     dict[p[j]]=dict[p[j]]-1   
#                     c+=1
#                 if c==len(p):
#                     list.append(i)
      
#             l=l+1
#             r=r+1
#         return (list)
# ## NOT EFFICIENT
       
            
        