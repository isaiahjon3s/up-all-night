"""
A simple linked list implementation with Node and LinkedList classes.
"""

from typing import Optional, Any


class Node:
    """A node in a linked list containing data and a reference to the next node."""
    
    def __init__(self, data: Any) -> None:
        """Initialize a new node with data.
        
        Args:
            data: The data to store in this node.
        """
        self.data = data
        self.next: Optional['Node'] = None

class LinkedList:
    """A simple singly linked list implementation."""
    
    def __init__(self) -> None:
        """Initialize an empty linked list."""
        self.head: Optional[Node] = None

    def append(self, data: Any) -> None:
        """Add a new node with the given data to the end of the list.
        
        Args:
            data: The data to add to the list.
        """
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self) -> None:
        """Print the contents of the linked list in a readable format."""
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements) + " -> None")

def main() -> None:
    """Demonstrate the LinkedList functionality."""
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.display()


if __name__ == "__main__":
    main()