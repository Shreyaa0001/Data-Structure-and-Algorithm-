class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None

def create():
    n = int(input("Enter a nodes 0 to stop: "))
    if n == 0:
        return None
    root = Node(n)
    print(f"Enter left child of {n}")
    root.left= create()
    print(f"Enter right child of {n}")
    root.right= create()
    return root

def preorder(root):
    if root is not None:
        print(root.data)
        preorder(root.left)
        preorder(root.right)

def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data)
        inorder(root.right)

def postorder(root):
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        print(root.data)

root = create()
print("Preorder Traversal: ")
preorder(root)
print("Inorder Traversal: ")
inorder(root)
print("Postorder Traversal: ")
postorder(root)