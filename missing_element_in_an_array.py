def missingNum(self, arr):
        # code here
        n=len(arr)+1
        sum=(n*(n+1))//2
        s2=0
        for i in arr:
            s2+=i
        return (sum-s2)
        