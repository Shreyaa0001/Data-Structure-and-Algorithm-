#Q.18 Decision Support System:A decision tree contains various choices and outcomes. Write a program to implement all three 
# recursive traversals—Inorder, Preorder, and Postorder.

class DecisionNode:
    def __init__(self, data):
        self.data = data      
        self.left = None      
        self.right = None     


def create_decision_tree():
    
    x = input("Enter choice/outcome (or 'end' for no node): ").strip()

    if x.lower() == "end":
        return None

    root = DecisionNode(x)

    print(f"Enter LEFT (No) branch of '{x}' ")
    root.left = create_decision_tree()

    print(f"Enter RIGHT (Yes) branch of '{x}' ")
    root.right = create_decision_tree()

    return root


def inorder_traversal(node):
    if node is not None:
        inorder_traversal(node.left)
        print(node.data, end=" | ")
        inorder_traversal(node.right)

print("/n")
def preorder_traversal(node):
    if node is not None:
        print(node.data, end=" | ")
        preorder_traversal(node.left)
        preorder_traversal(node.right)

print("/n")
def postorder_traversal(node):
    if node is not None:
        postorder_traversal(node.left)
        postorder_traversal(node.right)
        print(node.data, end=" | ")

print("/n")
def build_sample_tree():
   
    root = DecisionNode("Income > 50k?")

    root.left = DecisionNode("Has collateral?")
    root.left.left = DecisionNode("Outcome: REJECT")
    root.left.right = DecisionNode("Outcome: APPROVE (secured loan)")

    root.right = DecisionNode("Credit score > 700?")
    root.right.left = DecisionNode("Outcome: APPROVE (higher interest)")
    root.right.right = DecisionNode("Outcome: APPROVE (best rate)")

    return root


if __name__ == "__main__":
    print("Decision Support System")
    print("1. Build tree manually")
    print("2. Use sample loan-approval decision tree")
    choice = input("Choose an option (1/2): ").strip()

    if choice == "1":
        print("\n-- Build your decision tree --")
        decision_root = create_decision_tree()
    else:
        decision_root = build_sample_tree()

    print("\nInorder Traversal (Left -> Node -> Right):")
    inorder_traversal(decision_root)

    print("\n\nPreorder Traversal (Node -> Left -> Right):")
    preorder_traversal(decision_root)

    print("\n\nPostorder Traversal (Left -> Right -> Node):")
    postorder_traversal(decision_root)
    print()