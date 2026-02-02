class Solution:
    def findUnion(self, a, b):
        Union = []
        i, j = 0, 0
        n=len(a)
        m=len(b)
        while i < n and j < m:
            if a[i] < b[j]:
                if not Union or Union[-1] != a[i]:
                    Union.append(a[i])
                i += 1
            elif b[j] < a[i]:
                if not Union or Union[-1] != b[j]:
                    Union.append(b[j])
                j += 1
            else:
                if not Union or Union[-1] != a[i]:
                    Union.append(a[i])
                i += 1
                j += 1
        while i < n:
            if not Union or Union[-1] != a[i]:
                Union.append(a[i])
            i += 1
        while j < m:
            if not Union or Union[-1] != b[j]:
                Union.append(b[j])
            j += 1
        return Union


        