class Solution:
    def quickSort(self, arr, low, high):
        #code here
        if low<high:
            pIndex=self.partition(arr,low,high)
            self.quickSort(arr,low,pIndex-1)
            self.quickSort(arr,pIndex+1,high)

    def partition(self, arr, low, high):
        #code here
        pivot=arr[low]
        i=low
        j=high
        while i<j:
            while i<=high and arr[i]<=pivot:
                i+=1
            while j>=low and arr[j]>pivot:
                j-=1
            if i<j:
                temp=arr[i]
                arr[i]=arr[j]
                arr[j]=temp
        temp=arr[low]
        arr[low]=arr[j]
        arr[j]=temp
        return j