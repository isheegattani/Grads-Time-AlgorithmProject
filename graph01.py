from collections import defaultdict

#Representation of graph
class Graph:
	def __init__(self,vertices,nodes):
		self.graph = defaultdict(list) #dictionary with adjacency List
		self.V = vertices #Number of vertices
		self.nodes=nodes

	# Function to add an edge
	def addEdge(self,u,v):
		self.graph[u].append(v)

	# A function used for topologicalSort
	def topologicalSortUtil(self,v,visited,stack):




		visited[v]="1"#current node is marked visited

		# Iteration for vertices adjacent to this vertex
		for i in self.graph[v]:
			if visited[i] == "0":
				self.topologicalSortUtil(i,visited,stack)

		# Current vertex is pushed to stack
		stack.insert(0,v)

	def topologicalSort(self):#Recursive function for topological sort

		visited={}
		visited=dict.fromkeys(self.nodes)
         #Initialize all vertices as not visited
		for key in visited:
			visited[key]="0"
		stack =[]

		# Call the recursive Topological function for all vertices one by one
		for i in nodes:
			if visited[i] == "0":
				self.topologicalSortUtil(i,visited,stack)
		return stack

	def longestPath(self,start,end): #longestpath function to compute the longest path and print it

		dist={}
		comesfrom = {}
		toponode = self.topologicalSort()
		print("Topological Sorting:")
		print(toponode)
		dist=dict.fromkeys(toponode)

		for key in dist:
			dist[key]=0


		for u in toponode:
			for v in self.graph[u]:
				if (int(dist[v]) < int(dist[u]) + 1):
					dist[v] = int(dist[u]) + 1
					comesfrom[v] = u

		maxpath=[]
		maxpath = [end]
		while maxpath[-1] != start:
				maxpath.append(comesfrom[maxpath[-1]])

		maxpath.reverse()
		print("Length of the Longest path:")
		print(dist[end])
		print("The Longest path")
		print(maxpath)

nodes=[1,2,3,4,5,6]
g= Graph(6,nodes)


g.addEdge(1,2);
g.addEdge(2,3);
g.addEdge(2,4);
g.addEdge(4,5);
g.addEdge(5,6);



print ("Following is a Topological Sort of the given graph")
g.topologicalSort()
g.longestPath(1,6)
