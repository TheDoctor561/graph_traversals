from collections import defaultdict
import unittest

# this is a dfs algorithm for a directed graph with 
class DFS: 
  def __init__(self, edges): 

    self.adj = defaultdict(list)
    # STEP 1: Convert edge list to dictionary assuming good input 
    for a,b in edges: 
      self.adj[a].append(b)
      self.adj[b].append(a)
    
  # Step 2. return if two nodes are connected using a directed graph 
  def dfs(self, a, b, ): 
    return self.dfsh(a, b, set())

  def dfsh(self, a, b, visit): 
    if a == b: 
      return True 
    
    if a in visit: 
      return False

    visit.add(a)
    for n in self.adj[a]:
      if self.dfsh(n, b, visit): 
        return True 
    return False 
  

class DFSTesting(unittest.TestCase): 
  def test_connected(self):
    edges = [[0, 1], [0, 2], [3, 4], [4, 5], [2,3]]
    d = DFS(edges)
    self.assertTrue(d.dfs(0,1))
    self.assertTrue(d.dfs(0,2))
    self.assertTrue(d.dfs(3,4))
    self.assertTrue(d.dfs(5,4))
    self.assertTrue(d.dfs(0,5))


  def test_basic(self):
    edges = [[0, 1], [0, 2], [3, 4], [4, 5]]
    d = DFS(edges)
    self.assertTrue(d.dfs(0,1))
    self.assertTrue(d.dfs(0,2))
    self.assertTrue(d.dfs(3,4))
    self.assertTrue(d.dfs(5,4))
    self.assertFalse(d.dfs(0,5))

if __name__ == '__main__':
    unittest.main()