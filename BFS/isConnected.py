from collections import defaultdict
from collections import deque
import unittest

class BFS: 
    def __init__(self, edges): 
        self.adj = defaultdict(list)
        for a, b in edges: 
            self.adj[a].append(b)
            self.adj[b].append(a)
    def isConnected(self, a, b): 
        q = deque()
        q.append(a)
        visited = set()
        
        while q: 
            curr = q.popleft()
            if curr not in visited: 
                if curr == b: 
                    return True 
                visited.add(curr)
                for i in self.adj[curr]: 
                    q.append(i)
        return False 


class BFSTesting(unittest.TestCase): 
  def test_connected(self):
    edges = [[0, 1], [0, 2], [3, 4], [4, 5], [2,3]]
    d = BFS(edges)
    self.assertTrue(d.isConnected(0,1))
    self.assertTrue(d.isConnected(0,2))
    self.assertTrue(d.isConnected(3,4))
    self.assertTrue(d.isConnected(5,4))
    self.assertTrue(d.isConnected(0,5))


  def test_basic(self):
    edges = [[0, 1], [0, 2], [3, 4], [4, 5]]
    d = BFS(edges)
    self.assertTrue(d.isConnected(0,1))
    self.assertTrue(d.isConnected(0,2))
    self.assertTrue(d.isConnected(3,4))
    self.assertTrue(d.isConnected(5,4))
    self.assertFalse(d.isConnected(0,5))

if __name__ == '__main__':
    unittest.main()