class Solution:
    def search(self, arr, x):
        # code here
        n=len(arr)
        for i in range(n):
            if arr[i]==x:
                return i
        return -1
        