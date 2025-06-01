import os
from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    def addEdge(self,u,v):
        self.graph[u].append(v)

    def display(self):
        for key,value in self.graph.items():
            print(key,value)
    def dfs_util(self,v,visisted:set):
        visisted.add(v)
        print(v)
        for neighbour in self.graph[v]:
            if neighbour not in visisted:
                self.dfs_util(neighbour,visisted)

    def dfs(self,v):
        visited = set()
        self.dfs_util(v,visited)


if __name__ == "__main__":
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)
    g.display()
    print("****")
    g.dfs(2)
    print("*****")
    

