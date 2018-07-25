from collections import defaultdict
class Graph:

	def __init__(self): 
		self.graph = self.defaultdict(list)

	def add_edge(self,u,v): 
		self.graph[u].append(v)

    def dfs_utility(self,i,visited):
	    visited[start] = True
	    print(i)
	    for i in arr[start]:
		    if visited[i] == False:
			    self.dfs_utility(i,visited)

    def depth_first_search(self): 
# fist we will make every unvisited node false    	
	    visited = [False for i in range(len(self.graph))]
#if graph is diconnected graph
	    for i in self.graph:
	    	if visited[i] == False:
		        self.dfs_utility(i,visited)

g = Graph()
g.add_edge(1,2)
g.add_edge(1,7)
g.add_edge(1,8)
g.add_edge(2,3)
g.add_edge(2,6)
g.add_edge(3,4)
g.add_edge(3,5)
g.add_edge(8,9)
g.add_edge(8,12)
g.add_edge(9,10)
print('the following depth first traversal')
g.depth_first_search()
