class Solution:
    def compress(self, chars: List[str]) -> int:
        i,j=0,0
        s=[]

        while j<len(chars):

            while j<len(chars) and chars[i]==chars[j]:
                j+=1
            
            s.append(chars[i])

            if j-i!=1:
                for c in str(j-i):
                    s.append(c)
            i=j

        chars[:]=s
        return len(s)
        
