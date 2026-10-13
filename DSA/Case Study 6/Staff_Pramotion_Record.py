class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, x):
    if root is None:
        return Node(x)
    if root.data > x:
        root.left = insert(root.left, x)
    else:
        root.right = insert(root.right, x)
    return root

def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

class Queue:
    def __init__(self):
        self.R = -1
        self.F = -1
        self.QT = [0] * 50   # larger size for employees

    def insert(self, x):
        if self.R == len(self.QT) - 1:
            print("Queue overflow...")
            return
        self.R += 1
        self.QT[self.R] = x
        if self.F == -1:
            self.F = 0

    def delete(self):
        if self.F == -1:
            print("Queue underflow...")
            return None
        y = self.QT[self.F]
        if self.F == self.R:
            self.F = -1
            self.R = -1
        else:
            self.F += 1
        return y

def level_wise(root):
    if root is None:
        print("Promotion registry is empty.")
        return
    q = Queue()
    q.insert(root)
    while q.F != -1:
        r = q.delete()
        print(r.data, end=" ")
        if r.left is not None:
            q.insert(r.left)
        if r.right is not None:
            q.insert(r.right)

def height(root):
    if root is None:
        return 0
    left_height = height(root.left)
    right_height = height(root.right)
    return max(left_height, right_height) + 1

def leaf_nodes(root):
    if root is None:
        return
    if root.left is None and root.right is None:
        print(root.data, end=" ")
    leaf_nodes(root.left)
    leaf_nodes(root.right)

# ---------------- MENU-DRIVEN MAIN ----------------
if __name__ == "__main__":
    root = None
    while True:
        print("\n--- Staff Promotion Records Menu ---")
        print("1. Insert Eligible Employee ID")
        print("2. Display Inorder Traversal (sorted IDs)")
        print("3. Display Level-wise Traversal")
        print("4. Display Height of Registry")
        print("5. Display Leaf Employee IDs")
        print("6. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            x = int(input("Enter Employee ID to insert: "))
            root = insert(root, x)
        elif choice == 2:
            print("Inorder traversal: ", end="")
            inorder(root)
            print()
        elif choice == 3:
            print("Level-wise traversal: ", end="")
            level_wise(root)
            print()
        elif choice == 4:
            print("Height of registry:", height(root))
        elif choice == 5:
            print("Leaf Employee IDs: ", end="")
            leaf_nodes(root)
            print()
        elif choice == 6:
            print("Exiting Staff Promotion Records...")
            break
        else:
            print("Invalid choice, try again.")




====================================================================================================================================================================

--- Staff Promotion Records Menu ---
1. Insert Eligible Employee ID
2. Display Inorder Traversal (sorted IDs)
3. Display Level-wise Traversal
4. Display Height of Registry
5. Display Leaf Employee IDs
6. Exit
Enter your choice: 1
Enter Employee ID to insert: 1001

--- Staff Promotion Records Menu ---
1. Insert Eligible Employee ID
2. Display Inorder Traversal (sorted IDs)
3. Display Level-wise Traversal
4. Display Height of Registry
5. Display Leaf Employee IDs
6. Exit
Enter your choice: 1
Enter Employee ID to insert: 1002

--- Staff Promotion Records Menu ---
1. Insert Eligible Employee ID
2. Display Inorder Traversal (sorted IDs)
3. Display Level-wise Traversal
4. Display Height of Registry
5. Display Leaf Employee IDs
6. Exit
Enter your choice: 1
Enter Employee ID to insert: 1003

--- Staff Promotion Records Menu ---
1. Insert Eligible Employee ID
2. Display Inorder Traversal (sorted IDs)
3. Display Level-wise Traversal
4. Display Height of Registry
5. Display Leaf Employee IDs
6. Exit
Enter your choice: 2
Inorder traversal: 1001 1002 1003 

--- Staff Promotion Records Menu ---
1. Insert Eligible Employee ID
2. Display Inorder Traversal (sorted IDs)
3. Display Level-wise Traversal
4. Display Height of Registry
5. Display Leaf Employee IDs
6. Exit
Enter your choice: 3
Level-wise traversal: 1001 1002 1003 

--- Staff Promotion Records Menu ---
1. Insert Eligible Employee ID
2. Display Inorder Traversal (sorted IDs)
3. Display Level-wise Traversal
4. Display Height of Registry
5. Display Leaf Employee IDs
6. Exit
Enter your choice: 4
Height of registry: 3

--- Staff Promotion Records Menu ---
1. Insert Eligible Employee ID
2. Display Inorder Traversal (sorted IDs)
3. Display Level-wise Traversal
4. Display Height of Registry
5. Display Leaf Employee IDs
6. Exit
Enter your choice: 5
Leaf Employee IDs: 1003 

--- Staff Promotion Records Menu ---
1. Insert Eligible Employee ID
2. Display Inorder Traversal (sorted IDs)
3. Display Level-wise Traversal
4. Display Height of Registry
5. Display Leaf Employee IDs
6. Exit
Enter your choice: 6
Exiting Staff Promotion Records...
