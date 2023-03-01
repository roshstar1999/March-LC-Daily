def sortArray(self, nums: List[int]) -> List[int]:
        temp=[0]*len(nums)

        def merge(left,mid,right):
            i=left
            j=mid+1
            n1=mid-left+1
            n2=right-mid

            for x in range(n1):
                temp[i+x]=nums[i+x]
            for x in range(0,n2):
                temp[j+x]=nums[j+x]
            
            start=left
            while i<mid+1 and j<right+1 :
                if temp[i]<temp[j]:
                    nums[start]=temp[i]
                    i+=1
                
                else:
                    nums[start]=temp[j]
                    j+=1

                start+=1
            
            while i<mid+1:
                nums[start]=temp[i]
                i+=1
                start+=1
            
            while j<right+1:
                nums[start]=temp[j]
                start+=1
                j+=1
        
        def mergeSort(left,right):

            if left>=right:
                return 
            mid=(left+right)//2

            mergeSort(left,mid)
            mergeSort(mid+1,right)

            merge(left,mid,right)

        mergeSort(0,len(nums)-1)
        return nums
