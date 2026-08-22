# Q.6 File Directory System:
# Files and folders are represented using a binary tree.
# This program implements NON-RECURSIVE postorder traversal
# using the two-stack method.

class FileNode:
    def __init__(self, data):
        self.data = data      
        self.left = None
        self.right = None


def create_directory_tree():
    
    x = input("Enter file/folder name (or 'end' for no node): ").strip()

    if x.lower() == "end":
        return None

    root = FileNode(x)

    print(f" Enter LEFT child of '{x}' ")
    root.left = create_directory_tree()

    print(f" Enter RIGHT child of '{x}' ")
    root.right = create_directory_tree()

    return root


def postorder_two_stacks(root):
   
    if root is None:
        return []

    stack1 = [root]
    stack2 = []
    result = []

    while stack1:
        node = stack1.pop()
        stack2.append(node)

        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)

    while stack2:
        result.append(stack2.pop().data)

    return result


def build_sample_tree():
   
    root = FileNode("root")
    root.left = FileNode("Documents")
    root.right = FileNode("Pictures")

    root.left.left = FileNode("resume.pdf")
    root.left.right = FileNode("notes.txt")

    root.right.right = FileNode("vacation.jpg")

    return root


if __name__ == "__main__":
    print("File Directory System")
    print("1. Build directory tree manually")
    print("2. Use sample directory tree")
    choice = input("Choose an option (1/2): ").strip()

    if choice == "1":
        print("\n-- Build your directory tree --")
        dir_root = create_directory_tree()
    else:
        dir_root = build_sample_tree()

    print("\nNon-recursive Postorder Traversal (two-stack method):")
    print(" | ".join(postorder_two_stacks(dir_root)))

