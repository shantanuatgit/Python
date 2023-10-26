class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class DoublyLinkedListNode:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

def binary_tree_to_doubly_linked_list(root, prev=None, dll=None):
    if root is None:
        return dll

    # Recursively convert left subtree
    dll = binary_tree_to_doubly_linked_list(root.left, prev, dll)

    # Convert the current node
    new_dll_node = DoublyLinkedListNode(root.value)
    if prev is not None:
        prev.next = new_dll_node
        new_dll_node.prev = prev
    else:
        dll.head = new_dll_node
    dll.tail = new_dll_node

    # Recursively convert right subtree
    dll = binary_tree_to_doubly_linked_list(root.right, new_dll_node, dll)

    return dll

# Helper function to print the doubly linked list
def print_doubly_linked_list(dll):
    current = dll.head
    while current:
        print(current.value, end=" <-> ")
        current = current.next
    print("None")

# Create a binary tree
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)

# Convert the binary tree to a doubly linked list
dll = DoublyLinkedList()
dll = binary_tree_to_doubly_linked_list(root, None, dll)

# Print the doubly linked list
print("Doubly Linked List:")
print_doubly_linked_list(dll)
