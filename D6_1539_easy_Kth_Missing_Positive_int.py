class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        i=1
        x=1
        j=0
        while i<arr[-1]:
            if i==arr[j]:
                j+=1
                
            else:
                if x==k:
                    return i
                x+=1
            i+=1
        
        while x<=k:

            i+=1
            x+=1
        return i
        
