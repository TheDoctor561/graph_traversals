# 1 Sort the edges in ascending order by weight 
# 2 Add edges in that order into the minimum spanning Tree. Skip the edges that would produce a cycle 
# 3 Repeat step 2 until n-1 edges are added 

class UnionFind: 
  def __init__(self, size): 
    self.root = [i for i in range(size)]
    self.rank = [0] * size

  def find(self, n):
    if self.root[n] != n: 
      self.root[n] = self.find(self.root[n])
    return self.root[n]
  
  def union(self, a, b): 
    fa = self.find(a)
    fb = self.find(b)

    if fa != fb: 
      if self.rank[fa] > self.rank[fb]: 
        self.root[fb] = fa
      elif self.rank[fa] < self.rank[fb]: 
        self.root[fa] = fb
      else: 
        self.root[fa] = fb
        self.rank[fa] += 1 
      return True 
    else: 
      return False

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        all_edges = []
        
        # Storing all edges of our complete graph.
        for curr_node in range(n): 
            for next_node in range(curr_node + 1, n): 
                weight = abs(points[curr_node][0] - points[next_node][0]) +\
                         abs(points[curr_node][1] - points[next_node][1])
                all_edges.append((weight, curr_node, next_node))
      
        
        # Sort all edges in increasing order.
        all_edges.sort()
        
        uf = UnionFind(n)
        mst_cost = 0
        edges_used = 0
        
        for weight, node1, node2 in all_edges:
            if uf.join(node1, node2):
                mst_cost += weight
                edges_used += 1
                if edges_used == n - 1:
                    break
        return mst_cost