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


nodes=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49]
g= Graph(50,nodes)



g.addEdge(0,1);
g.addEdge(0,3);
g.addEdge(1,2);
g.addEdge(1,4);
g.addEdge(2,5);
g.addEdge(3,6);
g.addEdge(4,7);
g.addEdge(5,7);
g.addEdge(6,7);
g.addEdge(7,8);
g.addEdge(8,9);
g.addEdge(9,10);
g.addEdge(10,11);
g.addEdge(10,13);
g.addEdge(11,12);
g.addEdge(11,14);
g.addEdge(12,15);
g.addEdge(13,16);
g.addEdge(14,17);
g.addEdge(15,17);
g.addEdge(16,17);
g.addEdge(17,18);
g.addEdge(18,19);
g.addEdge(19,20);
g.addEdge(20,21);
g.addEdge(20,23);
g.addEdge(21,22);
g.addEdge(21,24);
g.addEdge(22,25);
g.addEdge(23,26);
g.addEdge(24,27);
g.addEdge(25,27);
g.addEdge(26,27);
g.addEdge(27,28);
g.addEdge(28,29);
g.addEdge(29,30);
g.addEdge(30,31);
g.addEdge(30,33);
g.addEdge(31,32);
g.addEdge(31,34);
g.addEdge(32,35);
g.addEdge(33,36);
g.addEdge(34,37);
g.addEdge(35,37);
g.addEdge(36,37);
g.addEdge(37,38);
g.addEdge(38,39);
g.addEdge(39,40);
g.addEdge(40,41);
g.addEdge(40,43);
g.addEdge(41,42);
g.addEdge(41,44);
g.addEdge(42,45);
g.addEdge(43,46);
g.addEdge(44,47);
g.addEdge(45,47);
g.addEdge(46,47);
g.addEdge(47,48);
g.addEdge(48,49);




print ("Following is a Topological Sort of the given graph")
g.topologicalSort()
g.longestPath(0,49)
