class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def insert(root,x):
    if root == None:
        return Node(x)    
    if root.data > x:
        root.left = insert(root.left,x)
    else:
        root.right = insert(root.right,x) 
    return root     
def create():
    root = None
    while True:
        x = int(input("Enter the element to be inserted (-1 to stop): "))
        if x == -1:
            break
        root = insert(root,x)         
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
        self.QT = [0]*5
    def insert(self,x):
        if self.R==4:
            print("Queue is overflow...")
            return
        self.R = self.R+1
        self.QT[self.R] = x
        if self.F == -1:
            self.F = 0
    def delete(self):
        if self.F== -1:
            print("Queue is underflow...")
            return
        else:
            y = self.QT[self.F]
            if self.F == self.R:
                self.F = -1
                self.R = -1
            else:
                self.F = self.F+1
        return y
    def peek(self):
        if self.F == -1:
            print("Queue is empty...")
            return
        else:
            return self.QT[self.F]
    def display(self):
        if self.F == -1:
            print("Nothing to display...")
            return
        for i in range(self.F,self.R+1):
             print(self.QT[i])
             
def level_wise(root):
    if root is None:
        return
    q = Queue()
    q.insert(root)
    while q.F != -1:
        r = q.delete()
        print(r.data, end=" ")
        if r.left != None:
            q.insert(r.left)
        if r.right != None:
            q.insert(r.right)
def height(root):
    if root is None:
        return 0
    else:
        left_height = height(root.left)
        right_height = height(root.right)
    return max(left_height, right_height) + 1    
def leaf_nodes(root):
    if root is None:
        return
    if root.left == None and root.right == None:
        print(root.data)
    
    leaf_nodes(root.left)
    leaf_nodes(root.right)

r = create()
print("\nInorder traversal of the tree is: ")
inorder(r)
print("\nLevel wise traversal of the tree is: ")            
level_wise(r)
print("\nHeight of the tree is: ")
print(height(r))
print("Leaf nodes of the tree are: ")
leaf_nodes(r)