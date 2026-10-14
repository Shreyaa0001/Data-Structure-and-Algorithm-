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
