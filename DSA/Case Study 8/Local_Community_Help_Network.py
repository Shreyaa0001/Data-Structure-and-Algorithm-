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

=================================================================================================================================================================
PS C:\Users\ASUS\AppData\Local\Programs\Microsoft VS Code> & C:\Users\ASUS\AppData\Local\Programs\Python\Python314\python.exe "c:/Users/ASUS/Advance Python/DSA/Case Study 8/Local_Community_Help_Network.py"
Enter no. of edges: 5
Enter Edge 1
Enter starting vertex: 0
Enter end vertex: 1
Enter Edge 2
Enter starting vertex: 1
Enter end vertex: 2
Enter Edge 3
Enter starting vertex: 2
Enter end vertex: 3
Enter Edge 4
Enter starting vertex: 3
Enter end vertex: 4
Enter Edge 5
Enter starting vertex: 4
Enter end vertex: 0
0 -> [1, 4]
1 -> [0, 2]
2 -> [1, 3]
3 -> [2, 4]
4 -> [3, 0]
Enter start resident: 0

BFS Traversal (Residents by Level):
Resident 0 at level 0
Resident 1 at level 1
Resident 4 at level 1
Resident 2 at level 2
Resident 3 at level 2
