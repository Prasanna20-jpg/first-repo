class Solution:
	def pushZerosToEnd(self, arr):
    	j=0
    	n=len(arr)
    	for i in range(n):
    	    if arr[i]!=0:
        	    arr[j]=arr[i]
        	    j+=1
    	for i in range(j,n):
    	    arr[i]=0
    	return arr
    	    