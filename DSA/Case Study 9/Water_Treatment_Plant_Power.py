class Graph:
    def __init__(self):
        self.v = 0
        self.e = 0
        self.G = []

    def create(self):
        self.v = int(input("Enter no. of vertices: "))
        self.e = int(input("Enter no. of edges: "))
        self.G = [[0 for _ in range(self.v)] for _ in range(self.v)]

        for i in range(self.e):
            print(f"\nEnter Edge {i+1}")
            u = int(input("Enter start vertex: "))
            v = int(input("Enter end vertex: "))
            w = int(input("Enter weight: "))
            self.G[u][v] = self.G[v][u] = w   # undirected

    def display(self):
        print("\nAdjacency Matrix:")
        for i in range(self.v):
            for j in range(self.v):
                print(self.G[i][j], end=" ")
            print()

    def prims(self):
        selected = [False] * self.v
        key = [float('inf')] * self.v
        parent = [-1] * self.v

        key[0] = 0   # start from vertex 0

        for _ in range(self.v):
            # pick minimum key vertex not yet included
            min_weight = float('inf')
            u = -1
            for j in range(self.v):
                if not selected[j] and key[j] < min_weight:
                    min_weight = key[j]
                    u = j

            selected[u] = True

            # update neighbors
            for v in range(self.v):
                if self.G[u][v] != 0 and not selected[v] and self.G[u][v] < key[v]:
                    key[v] = self.G[u][v]
                    parent[v] = u

        # print MST edges and cost
        total = 0
        print("\nEdges in MST:")
        for i in range(1, self.v):
            print(parent[i], "-", i, ":", self.G[i][parent[i]])
            total += self.G[i][parent[i]]
        print("Total wiring cost =", total)


# Driver code
obj = Graph()
obj.create()
obj.display()
obj.prims()

=================================================================================================================================================================
PS C:\Users\ASUS\AppData\Local\Programs\Microsoft VS Code> & C:\Users\ASUS\AppData\Local\Programs\Python\Python314\python.exe "c:/Users/ASUS/Advance Python/DSA/Case Study 9/Water_Treatment_Plant_Power.py"
Enter no. of vertices: 4
Enter no. of edges: 5

Enter Edge 1
Enter start vertex: 0
Enter end vertex: 1
Enter weight: 10

Enter Edge 2
Enter start vertex: 0
Enter end vertex: 2
Enter weight: 6

Enter Edge 3
Enter start vertex: 0
Enter end vertex: 3
Enter weight: 5

Enter Edge 4
Enter start vertex: 1
Enter end vertex: 3
Enter weight: 15

Enter Edge 5
Enter start vertex: 2
Enter end vertex: 3
Enter weight: 4

Adjacency Matrix:
0 10 6 5 
10 0 0 15 
6 0 0 4 
5 15 4 0 

Edges in MST:
0 - 1 : 10
3 - 2 : 4
0 - 3 : 5
Total wiring cost = 19
