def findUnique(self, arr):
        xor=0
        n=len(arr)
        for i in range(n):
            xor=xor^arr[i]
        return xor