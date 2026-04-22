def canPartition(nums):
    total=sum(nums)
    if total%2:
        return False
    target=total//2
    n=len(nums)
    dp={}

    def solve(i,t):
        if t==0:
            return True
        if i==0:
            return nums[0]==t
        if (i,t) in dp:
            return dp[(i,t)]
        not_take=solve(i-1,t)
        take=False
        if nums[i]<=t:
            take=solve(i-1,t-nums[i])
        dp[(i,t)]=take or not_take
        return dp[(i,t)]
    return solve(n-1,target)