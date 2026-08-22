# Non Recursive Preorder & Inorder Traversal in binary tree
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def create():
    x = int(input("Enter the data (-1 for no node): "))

    if x == -1:
        return None

    root = Node(x)

    print(f"Enter left of {x}")
    root.left = create()

    print(f"Enter right of {x}")
    root.right = create()

    return root

class Stack:
    def __init__(self):
        self.TOP = -1
        self.st = [0] * 100

    def push(self, x):
        if self.TOP == 99:
            print("Stack Overflow")
            return

        self.TOP += 1
        self.st[self.TOP] = x

    def pop(self):
        if self.TOP == -1:
            print("Stack Underflow")
            return

        x = self.st[self.TOP]
        self.TOP -= 1
        return x
def preorder(root):
    s=Stack() #object
    while root is not None:
        print(root.data)
        s.push(root)
        root=root.left
        while s.TOP!=-1:
           r= s.pop()
           r=r.right
           while r is not None:
                   print(r.data)
                   s.push(r)
                   r=r.left
def inorder(root):
    s1=Stack() #object of stack
    while root !=None:
        s1.push(root)
        root=root.left
    while s1.TOP!=-1:
        root=s1.pop()
        print(root.data)
        root=root.right
    while root !=None:
        s1.push(root)
        root=root.left
                    
node = create()
print("\nPreorder Traversal:")
preorder(node)
print("\nInorder Traversal:")
inorder(node)
                    
                    