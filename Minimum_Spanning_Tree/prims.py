class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n, ret, minHeap, visited = len(points), 0, [(0,0)], set()
        
        while len(visited) < n: 
            w, curr = heapq.heappop(minHeap)
            if curr in visited: 
                continue 
                
            ret += w 
            visited.add(curr)
            
            for nn in range(n): 
                if nn not in visited: 
                    ww = self.weight(points[nn], points[curr])
                    heapq.heappush(minHeap, (ww, nn))
                    
        return ret 
                
    def weight(self, p1, p2): 
        x1,x2,y1,y2 = p1[0],p2[0],p1[1],p2[1]
        return abs(x2-x1) + abs(y2-y1)
        