# Q.17 Digital Dictionary System: Numerical word identifiers are stored in a Binary Search Tree (BST).
# This program implements recursive PREORDER and POSTORDER traversals and displays the resulting sequences.

class WordNode:
    def __init__(self, word_id):
        self.data = word_id
        self.left = None
        self.right = None


class DictionaryBST:
    def __init__(self):
        self.root = None

    def insert(self, word_id):
        
        if self.root is None:
            self.root = WordNode(word_id)
        else:
            self._insert_recursive(self.root, word_id)

    def _insert_recursive(self, node, word_id):
        if word_id < node.data:
            if node.left is None:
                node.left = WordNode(word_id)
            else:
                self._insert_recursive(node.left, word_id)
        elif word_id > node.data:
            if node.right is None:
                node.right = WordNode(word_id)
            else:
                self._insert_recursive(node.right, word_id)
        # duplicate word IDs are ignored

    # ---------- Recursive Preorder ----------
    def preorder(self):
        result = []
        self._preorder_helper(self.root, result)
        return result

    def _preorder_helper(self, node, result):
        if node is not None:
            result.append(node.data)          
            self._preorder_helper(node.left, result)   
            self._preorder_helper(node.right, result)  

    # ---------- Recursive Postorder ----------
    def postorder(self):
        result = []
        self._postorder_helper(self.root, result)
        return result

    def _postorder_helper(self, node, result):
        if node is not None:
            self._postorder_helper(node.left, result)  
            self._postorder_helper(node.right, result) 
            result.append(node.data)           # Node


def build_sample_dictionary():
    """
    Sample word identifiers inserted into the BST:
    45, 20, 70, 10, 30, 60, 90, 5, 15
    """
    dictionary = DictionaryBST()
    for word_id in [45, 20, 70, 10, 30, 60, 90, 5, 15]:
        dictionary.insert(word_id)
    return dictionary


if __name__ == "__main__":
    print("Digital Dictionary System (BST of word identifiers)")
    print("1. Enter word identifiers manually")
    print("2. Use sample word identifiers")
    choice = input("Choose an option (1/2): ").strip()

    word_dict = DictionaryBST()

    if choice == "1":
        n = int(input("How many word identifiers to insert? "))
        for i in range(n):
            wid = int(input(f"Enter word identifier {i + 1}: "))
            word_dict.insert(wid)
    else:
        word_dict = build_sample_dictionary()
        print("Inserted word identifiers: 45, 20, 70, 10, 30, 60, 90, 5, 15")

    preorder_sequence = word_dict.preorder()
    postorder_sequence = word_dict.postorder()

    print("\nPreorder Traversal (Node -> Left -> Right):")
    print(preorder_sequence)

    print("\nPostorder Traversal (Left -> Right -> Node):")
    print(postorder_sequence)