""" DFS  Depth First Search is an algorithm for tree traversal on graph or tree data structures. 
It can be implemented using recursion and data structures like dictionaries and sets."""

""" The Algorithm: pick any node,if it's unvisited,mark it as visited and recur on all its adjacent nodes.
Repeat until all the nodes are visited,or node cannot be found."""

#This approach works for directed as well as undirected graphs
graph={'A':['B','C'],'B':['D','E'],'C':['F'],'D':[],'E':['F'],'F':[]}
visited=set() #set to keep track of visited nodes
def dfs1(visited,graph,node):
    if node not in visited:
        print(node)
        visited.add(node)
        print(visited)
        for neigh in graph[node]:
            dfs1(visited,graph,neigh)

dfs1(visited,graph,'A')     

#Time Complexity is O(V+E)