class Solution:
    def intersection(self, arr1, arr2):
        #code here
        i,j=0,0
        ans=[]
        n=len(arr1)
        m=len(arr2)
        while(i<n and j<m):
            if arr1[i]<arr2[j]:
                i+=1
            elif arr2[j]<arr1[i]:
                j+=1
            else :
                ans.append(arr1[i])
                val = arr1[i]
                while i < n and arr1[i] == val:
                    i += 1
                while j < m and arr2[j] == val:
                    j += 1
                
        return ans
            
    
