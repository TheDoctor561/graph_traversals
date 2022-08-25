from collections import defaultdict
import unittest

# Iterative version of Depth First Search 

class DFS:
  def __init__(self, edges): 
    self.adj = defaultdict(list)
    for a, b in edges: 
      self.adj[a].append(b)
      self.adj[b].append(a)

  def dfs(self, a, b): 
    return self.dfsh(a, b, set())
  
  def dfsh(self, a, b, seen):
    if a == b: 
      return True 
    
    stack = [a]
    while stack: 
      a = stack.pop()
      if a == b: 
        return True 
      
      seen.add(a)
      for node in self.adj[a]:
        if node not in seen: 
          stack.append(node)
  
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