class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        res=[0]*len(spells)
        potions.sort()
        n=len(spells)
        m=len(potions)

        for i in range(n):
            spell=spells[i]
            left=0
            right=m-1
            

            while left<=right:
                mid=(left+right)//2
                product=spells[i]*potions[mid]
                if success==product:
                    right= mid-1
                if success>product:
                    left=mid+1
                else:
                    right=mid-1

            res[i]=m-left
        return res
