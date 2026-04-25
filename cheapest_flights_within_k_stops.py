from collections import deque

class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        adj = [[] for _ in range(n)]
        for u, v, w in flights:
            adj[u].append((v, w))
        
        dist = [float('inf')] * n
        q = deque([(src, 0, 0)])   # FIXED
        
        while q:
            node, cost, stops = q.popleft()
            
            if stops > k:
                continue
            
            for nei, price in adj[node]:
                new_cost = cost + price
                if new_cost < dist[nei]:
                    dist[nei] = new_cost
                    q.append((nei, new_cost, stops + 1))  # FIXED
        
        return -1 if dist[dst] == float('inf') else dist[dst]