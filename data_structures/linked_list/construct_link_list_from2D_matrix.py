class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.down = None

class LinkedList:
    def __init__(self):
        self.head = None

def construct_linked_list(matrix):
    if not matrix:
        return None

    rows, cols = len(matrix), len(matrix[0])

    # Create a 2D array of nodes to represent the matrix
    nodes = [[Node(matrix[i][j]) for j in range(cols)] for i in range(rows)]

    # Connect the nodes to form the linked list
    for i in range(rows):
        for j in range(cols):
            if j < cols - 1:
                nodes[i][j].right = nodes[i][j + 1]
            if i < rows - 1:
                nodes[i][j].down = nodes[i + 1][j]

    # Create the linked list from the first row
    linked_list = LinkedList()
    linked_list.head = nodes[0][0]

    return linked_list

def print_linked_list(linked_list):
    current = linked_list.head
    while current:
        row_values = []
        while current:
            row_values.append(current.value)
            current = current.right
        print(" -> ".join(map(str, row_values)))
        current = current.down

# Example usage
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

linked_list = construct_linked_list(matrix)
print("Linked List Representation of the Matrix:")
print_linked_list(linked_list)
