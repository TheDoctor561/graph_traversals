# The vey basics of union find and disjoint sets 
# Basically an array and within that array lies a disjoint set 


# There are two functions when discussing disjoint sets 

# find(a) which takes in a single argument and returns the root of 
# that particular node 

# union(a,b) which takes in two arguments and combines them together 
# let's watch a quick video on how this works and then implement from there 

# First lets implement UnionFind as an object and instantiate it with an array 

class UnionFind: 
    def __init__(self, size):
        self.arr = [i for i in range(size)]


uu = UnionFind(5)

print(uu.arr)