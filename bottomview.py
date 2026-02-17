from collections import deque
class Solution:
    def bottomView(self,root):
        q=deque([(root,0)])
        d={}
        while(len(q)>0):
            node,vertical=q.popleft()
            if(node.left):
                q.append(node.left)
            if(node.right):
                q.append(node.right)
            d[vertical]=node.data
        ans=[]
        for i in sorted(d):
            ans.append(d[i])
        return ans