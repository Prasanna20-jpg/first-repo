class Solution:
    def findOrder(words):
        adj={}
        indegree={}
        for word in words:
            for c in word:
                if c not in adj:
                    adj[c]=[]
                if c not in adj:
                    adj[c]=[]
        for i in range(len(words)):
            w1=words[i]
            w2=words[i+1]
            ml=min(len(w1),len(w2))
            if len(w1)>len(w2) and w1[:ml]==w2[:ml]:
                return ""
            for j in range(ml):
                if w1[j]!=w2[j]:
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].append(w2[j])
                        indegree[w2[j]]+=1
                    break
            q=[]
            for c in indegree:
                if indegree[c]==0:
                    q.append(c)
            front=0
            res=[]
            while front<len(q):
                node=q[front]
                front+=1
                res.append(node)
                for nei in adj[node]:
                    indegree[nei]-=1
                    if indegree[nei]==0:
                        q.append(nei)
            if len(res)!=len(indegree):
                return ""
            return "".join(res)              
