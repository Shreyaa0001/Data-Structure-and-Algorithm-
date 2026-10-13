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

    def bfs(self, start):
        visited = [False] * self.vertices
        level = [0] * self.vertices
        queue = [start]   # use list as queue
        visited[start] = True

        print("\nBFS Traversal (Residents by Level):")
        while queue:
            current = queue.pop(0)   # dequeue front element
            print(f"Resident {current} at level {level[current]}")
            for neighbor in self.AdjL[current]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    level[neighbor] = level[current] + 1
                    queue.append(neighbor)   # enqueue neighbor


# ---- Driver Code ----
o = Graph(5)        # Example: 5 residents
o.addEdge()         # Add assistance/friendship connections
o.display()         # Show adjacency list
start = int(input("Enter start resident: "))
o.bfs(start)
