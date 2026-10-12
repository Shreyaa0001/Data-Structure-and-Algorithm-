class Graph:
    def __init__(self, v):
        self.vertices = v
        self.AdjL = [[] for i in range(v)]

    def addEdge(self):
        e = int(input("Enter no. of edges: "))
        for i in range(e):
            print(f"Enter Edge {i+1}")
            u = int(input("Enter starting vertex: "))
            v = int(input("Enter end vertex: "))
            self.AdjL[u].append(v)
            self.AdjL[v].append(u)  # undirected graph

    def display(self):
        for i in range(self.vertices):
            print(i, "->", self.AdjL[i])

    def dfs(self, start):
        visited = [False] * self.vertices
        stack = [start]   # use stack for DFS

        while stack:
            current = stack.pop()
            if not visited[current]:
                print(current, end=" ")
                visited[current] = True
                # push neighbors in reverse order for consistent traversal
                for vertex in reversed(self.AdjL[current]):
                    if not visited[vertex]:
                        stack.append(vertex)

o = Graph(3)        
o.addEdge()         
o.display()         
start = int(input("Enter start vertex: "))
print("DFS Traversal:")
o.dfs(start)
