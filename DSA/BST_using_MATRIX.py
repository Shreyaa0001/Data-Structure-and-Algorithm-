# From BST using Adjecency matrix
class Graph:
    def __init__(self):
        self.v = 0
        self.e = 0
        self.G = [[0 for i in range(9)] for j in range(9)]

    def create(self):
        self.v = int(input("Enter no of vertices:"))
        self.e = int(input("Enter no of edges:"))

        for i in range(self.e):
            print(f"Enter edge {i + 1}:")
            u = int(input("Enter start vertex:"))
            v = int(input("Enter End vertex:"))
            w = int(input("Enter weight:"))
            self.G[u][v] = self.G[v][u] = w  # Undirected
            # For directed non-weighted:
            # self.G[v][u] = 1

    def display(self):
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
            print("Stack is underflow")
            return
        x = self.st[self.TOP]
        self.TOP -= 1
        return x

def dfs(obj, start):
    visited = [False] * obj.v
    s = Stack()
    s.push(start)
    while s.TOP != -1:
        u = s.pop()
        if visited[u] == False:
            print(u, end=" ")
            visited[u] = True
            for v in range(obj.v - 1, -1, -1):
                if obj.G[u][v] != 0 and visited[v] == False:
                    s.push(v)

obj = Graph()
obj.create()
obj.display()
start = int(input("Enter start vertex:"))
dfs(obj, start)
###############################################################################################################################################################
-----------------------------OUTPUT--------------------

Enter no of vertices:3
Enter no of edges:3
Enter edge 1:
Enter start vertex:0
Enter End vertex:1
Enter weight:2
Enter edge 2:
Enter start vertex:1
Enter End vertex:2
Enter weight:4
Enter edge 3:
Enter start vertex:2
Enter End vertex:0
Enter weight:6
0 2 6 
2 0 4 
6 4 0 
Enter start vertex:0
0 2 
