class Graph:
    def __init__(self):
        self.v = 0
        self.e = 0
        self.G = []

    def create(self):
        self.v = int(input("Enter number of hubs (vertices): "))
        self.e = int(input("Enter number of connections (edges): "))
        self.G = [[0 for _ in range(self.v)] for _ in range(self.v)]

        for i in range(self.e):
            print(f"\nEnter Connection {i+1}")
            u = int(input("Enter start hub: "))
            v = int(input("Enter end hub: "))
            w = int(input("Enter cable cost: "))
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

        key[0] = 0   # start from hub 0

        for _ in range(self.v):
            # pick minimum key hub not yet included
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
        print("\nOptimal Connections (MST):")
        for i in range(1, self.v):
            print(parent[i], "-", i, ":", self.G[i][parent[i]])
            total += self.G[i][parent[i]]
        print("Total wiring cost =", total)

# Driver code
obj = Graph()
obj.create()
obj.display()
obj.prims()
===========================================================================================================================================================================
PS C:\Users\ASUS\AppData\Local\Programs\Microsoft VS Code> & C:\Users\ASUS\AppData\Local\Programs\Python\Python314\python.exe "c:/Users/ASUS/Advance Python/DSA/Case Study 9/Electric_Vehicle_Charging_Hubs.py"
Enter number of hubs (vertices): 4
Enter number of connections (edges): 5

Enter Connection 1
Enter start hub: 0
Enter end hub: 1
Enter cable cost: 8

Enter Connection 2
Enter start hub: 0
Enter end hub: 2
Enter cable cost: 5

Enter Connection 3
Enter start hub: 1
Enter end hub: 2
Enter cable cost: 9

Enter Connection 4
Enter start hub: 1
Enter end hub: 3
Enter cable cost: 11

Enter Connection 5
Enter start hub: 2
Enter end hub: 3
Enter cable cost: 7

Adjacency Matrix:
0 8 5 0 
8 0 9 11 
5 9 0 7 
0 11 7 0 

Optimal Connections (MST):
0 - 1 : 8
0 - 2 : 5
2 - 3 : 7
Total wiring cost = 20
