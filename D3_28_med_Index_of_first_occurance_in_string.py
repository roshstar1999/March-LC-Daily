class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        nlen=len(needle)
        hlen=len(haystack)
        i=0
        while i<hlen and hlen-i>=nlen:#doubt
            if needle[0]==haystack[i]:
                if needle==haystack[i:i+nlen]:
                    return i
                
            i+=1
        return -1
            
