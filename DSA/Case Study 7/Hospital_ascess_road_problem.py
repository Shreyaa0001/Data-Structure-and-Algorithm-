class Graph:
    def __init__(self):
        self.v = 0   # number of locations (entrances/departments)
        self.e = 0   # number of connecting roads
        self.G = [[0 for i in range(9)] for j in range(9)]  # adjacency matrix

    def create(self):
        self.v = int(input("Enter number of hospital locations: "))
        self.e = int(input("Enter number of connecting roads: "))

        for i in range(self.e):
            print(f"Enter road {i + 1}:")
            u = int(input("Enter start location: "))
            v = int(input("Enter end location: "))
            w = int(input("Enter distance (weight): "))
            self.G[u][v] = self.G[v][u] = w   # undirected road

    def display(self):
        print("\nAdjacency Matrix (Hospital Road Network):")
        for i in range(self.v):
            for j in range(self.v):
                print(self.G[i][j], end=" ")
            print()

class Stack:
    def __init__(self):
        self.st = []
        self.TOP = -1

    def push(self, x):
        self.st.append(x)
        self.TOP += 1

    def pop(self):
        if self.TOP == -1:
            print("Stack Underflow")
            return None
        x = self.st[self.TOP]
        self.TOP -= 1
        return x

def dfs(obj, start):
    visited = [False] * obj.v
    s = Stack()
    s.push(start)
    print("\nDFS Traversal from Main Entrance:")
    while s.TOP != -1:
        u = s.pop()
        if not visited[u]:
            print(u, end=" ")
            visited[u] = True
            for v in range(obj.v - 1, -1, -1):
                if obj.G[u][v] != 0 and not visited[v]:
                    s.push(v)

# Demo Run
obj = Graph()
obj.create()
obj.display()
start = int(input("Enter starting location (Main Entrance index): "))
dfs(obj, start)
