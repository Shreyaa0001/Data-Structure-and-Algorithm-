class BookNode:
    def __init__(self, book_id, title):
        self.book_id = book_id
        self.title = title
        self.left = None
        self.right = None
class LibraryCatalog:
    def __init__(self):
        self.root = None

    def insert(self, book_id, title):
        self.root = self._insert_recursive(self.root, book_id, title)

    def _insert_recursive(self, node, book_id, title):
        if node is None:
            return BookNode(book_id, title)
        if book_id < node.book_id:
            node.left = self._insert_recursive(node.left, book_id, title)
        else:
            node.right = self._insert_recursive(node.right, book_id, title)
        return node
    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(f"{node.book_id}: {node.title}")
            self.inorder(node.right)

    def preorder(self, node):
        if node:
            print(f"{node.book_id}: {node.title}")
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(f"{node.book_id}: {node.title}")

if __name__ == "__main__":
    catalog = LibraryCatalog()
    catalog.insert(50, "Data Structures")
    catalog.insert(30, "Algorithms")
    catalog.insert(70, "Operating Systems")
    catalog.insert(20, "Computer Networks")
    catalog.insert(40, "Database Systems")

    print("\nInorder Traversal (Sorted):")
    catalog.inorder(catalog.root)

    print("\nPreorder Traversal (Hierarchy):")
    catalog.preorder(catalog.root)

    print("\nPostorder Traversal (Cleanup):")
    catalog.postorder(catalog.root)


