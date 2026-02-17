class Solution:
    def generate(self,ind,curr_subset,ans,candidates,target):
        if(target==0):
            ans.append(curr_subset.copy())
            return
        if(target<0):
            return
        if(ind==len(candidates)):
            return
        curr_subset.append(candidates[ind])
        self.generate(ind,curr_subset,ans,candidates,target-candidates[ind])
        curr_subset.pop()
        self.generate(ind+1,curr_subset,ans,candidates,target)
    def combinationSum(self,candidates:List[int],target:int) -> List[List[int]]:
        ind=0
        curr_subset=[]
        ans=[]
        self.generate(ind,curr_subset,ans,candidates,target)
        return ans
