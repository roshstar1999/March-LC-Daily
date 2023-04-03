class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n=len(people)
        people.sort()
        start=0
        end=n-1
        count=0
        

        while start<=end:
            if people[start]+people[end]<=limit:
                count+=1
                start+=1
                end-=1
            else:
                count+=1
                end-=1
        return count
