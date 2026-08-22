# Q.9 Hospital Patient Record System: Patient IDs are stored in a Binary Search Tree (BST).
# This program implements BOTH recursive and non-recursive postorder traversal, then verifies both sequences match.

class PatientNode:
    def __init__(self, patient_id):
        self.data = patient_id
        self.left = None
        self.right = None


class PatientBST:
    def __init__(self):
        self.root = None

    def insert(self, patient_id):
        """Standard BST insertion, based on Patient ID."""
        if self.root is None:
            self.root = PatientNode(patient_id)
        else:
            self._insert_recursive(self.root, patient_id)

    def _insert_recursive(self, node, patient_id):
        if patient_id < node.data:
            if node.left is None:
                node.left = PatientNode(patient_id)
            else:
                self._insert_recursive(node.left, patient_id)
        elif patient_id > node.data:
            if node.right is None:
                node.right = PatientNode(patient_id)
            else:
                self._insert_recursive(node.right, patient_id)
        # duplicate patient IDs are ignored

    # ---------- Recursive Postorder ----------
    def postorder_recursive(self):
        result = []
        self._postorder_recursive_helper(self.root, result)
        return result

    def _postorder_recursive_helper(self, node, result):
        if node is not None:
            self._postorder_recursive_helper(node.left, result)
            self._postorder_recursive_helper(node.right, result)
            result.append(node.data)

    # ---------- Non-Recursive Postorder (two-stack method) ----------
    def postorder_non_recursive(self):
        if self.root is None:
            return []

        stack1 = [self.root]
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

    # ---------- Non-Recursive Postorder (single-stack method) ----------
    def postorder_non_recursive_single_stack(self):
        """
        Alternative single-stack approach, in case a purely single-stack
        method is required instead of the two-stack version above.
        Uses a 'last visited' pointer to decide when a node is ready
        to be added to the result.
        """
        if self.root is None:
            return []

        stack = []
        result = []
        current = self.root
        last_visited = None

        while stack or current:
            if current:
                stack.append(current)
                current = current.left
            else:
                peek_node = stack[-1]
                # If right child exists and hasn't been processed yet, go right
                if peek_node.right and last_visited != peek_node.right:
                    current = peek_node.right
                else:
                    result.append(peek_node.data)
                    last_visited = stack.pop()

        return result


def build_sample_bst():
    """
    Sample patient IDs inserted into the BST:
    50, 30, 70, 20, 40, 60, 80
    """
    bst = PatientBST()
    for patient_id in [50, 30, 70, 20, 40, 60, 80]:
        bst.insert(patient_id)
    return bst


if __name__ == "__main__":
    print("Hospital Patient Record System (BST)")
    print("1. Enter patient IDs manually")
    print("2. Use sample patient IDs")
    choice = input("Choose an option (1/2): ").strip()

    hospital_bst = PatientBST()

    if choice == "1":
        n = int(input("How many patient IDs to insert? "))
        for i in range(n):
            pid = int(input(f"Enter patient ID {i + 1}: "))
            hospital_bst.insert(pid)
    else:
        hospital_bst = build_sample_bst()
        print("Inserted patient IDs: 50, 30, 70, 20, 40, 60, 80")

    recursive_result = hospital_bst.postorder_recursive()
    non_recursive_result = hospital_bst.postorder_non_recursive()
    single_stack_result = hospital_bst.postorder_non_recursive_single_stack()

    print("\nRecursive Postorder Traversal:      ", recursive_result)
    print("Non-Recursive Postorder (2-stack):  ", non_recursive_result)
    print("Non-Recursive Postorder (1-stack):  ", single_stack_result)

    # ---------- Verification ----------
    if recursive_result == non_recursive_result == single_stack_result:
        print("\n Verification PASSED: All traversal sequences match.")
    else:
        print("\n Verification FAILED: Traversal sequences do NOT match.")