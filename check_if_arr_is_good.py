class Solution:
    def isGood(self, nums: List[int]) -> bool:
        arr=sorted(nums)
        count=0
        n=len(arr)
        maxElement=arr[n-1]
        if arr[0]!=1:
            return False
        if n == maxElement+1 :
            for i in range(1,n):
                if arr[i]==arr[i-1]+1:
                    count+=1
                elif arr[i] == maxElement and arr[i] == arr[i-1]:
                    count+=1
            if count == n-1:
                return True
        return False

                