class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sorteds=sorted(s)
        sortedt=sorted(t)

        n=len(s)
        for i in range(n):
            if sorteds[i]!=sortedt[i]:
                return sortedt[i]
        return sortedt[-1]






