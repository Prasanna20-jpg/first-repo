class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        n=len(nums)
        sum1=0
        sum2=0
        for i in range(n):
            if nums[i]<10:
                sum1+=nums[i]
            else:
                sum2+=nums[i]
        if sum1 == sum2:
            return False
        return True
