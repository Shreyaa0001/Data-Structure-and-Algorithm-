class Graph:
    def __init__(self):
        self.v = 0   # number of airport locations
        self.e = 0   # number of access roads
        self.G = [[0 for i in range(9)] for j in range(9)]  # adjacency matrix

    def create(self):
        self.v = int(input("Enter number of airport locations (entrance, terminals, parking): "))
        self.e = int(input("Enter number of access roads: "))

        for i in range(self.e):
            print(f"Enter road {i + 1}:")
            u = int(input("Enter start location: "))
            v = int(input("Enter end location: "))
            w = int(input("Enter distance (weight): "))
            self.G[u][v] = self.G[v][u] = w   # undirected road

    def display(self):
        print("\nAdjacency Matrix (Airport Road Network):")
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
    print("\nDFS Traversal from Airport Entrance:")
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
start = int(input("Enter starting location (Airport Entrance index): "))
dfs(obj, start)

===========================================================================================================================================================
PS C:\Users\ASUS\AppData\Local\Programs\Microsoft VS Code> & C:\Users\ASUS\AppData\Local\Programs\Python\Python314\python.exe "c:/Users/ASUS/Advance Python/DSA/Case Study 7/Airport_Road_Access.py"
Enter number of airport locations (entrance, terminals, parking): 3
Enter number of access roads: 3
Enter road 1:
Enter start location: 0
Enter end location: 1
Enter distance (weight): 3
Enter road 2:
Enter start location: 1
Enter end location: 2
Enter distance (weight): 5
Enter road 3:
Enter start location: 2
Enter end location: 0
Enter distance (weight): 8

Adjacency Matrix (Airport Road Network):
0 3 8 
3 0 5 
8 5 0 
Enter starting location (Airport Entrance index): 0

DFS Traversal from Airport Entrance:
0 2 
