class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n=len(nums)
        j=0
        i=0
        while i+1<n:
            if nums[i]==nums[i+1]:
                nums[i]*=2
                nums[i+1]=0
            i+=1
        for i in range(n):
            if nums[i]!=0:
                nums[j]=nums[i]
                j+=1
        for i in range(j,n):
            nums[i]=0
        return nums
