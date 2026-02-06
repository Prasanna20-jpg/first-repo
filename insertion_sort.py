class Solution:
    def insertionSort(self, arr):
        # code here
        n=len(arr)
        for i in range(0,n):
            j=i
            while j>0 and arr[j-1]>arr[j]:
                temp=arr[j-1]
                arr[j-1]=arr[j]
                arr[j]=temp
                j-=1