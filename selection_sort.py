class Solution: 
    def selectionSort(self, arr):
        #code here
        n=len(arr)
        for i in range(0,n-1,1):
            mini=i
            for j in range(i,n,1):
                if arr[j]<arr[mini]:
                    mini=j
            temp=arr[mini]
            arr[mini]=arr[i]
            arr[i]=temp
            