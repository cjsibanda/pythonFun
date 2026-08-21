# ============================================================
# Linked Lists in Python
# Concepts:
# - Nodes
# - Simple chain of objects
# - Adding/removing elements
# - Stack (LIFO)
# - Queue (FIFO)
#
# C++ -> Python:
# nullptr -> None
# Node*   -> object reference
# new     -> create object
# delete  -> Python garbage collector handles memory
# ============================================================

# ============================================================
# NODE
# ============================================================
class Node:
    #  node stores data and a reference to the next node
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node
# ============================================================
# SIMPLE LINKED LIST
# ============================================================
class LinkedList:

    def __init__(self):
        # Head points to the first node
        self.head = None

    def add_front(self, data):
        # Add a new node to the head of the list
        self.head = Node(data, self.head)

    def remove_front(self):
        # Remove the first node
        if self.head is None:
            return None

        value = self.head.data
        self.head = self.head.next
        return value

    def display(self):
        # Traverse from head to tail
        current = self.head

        while current:
            print(current.data, end=" ")
            current = current.next

        print()

# ============================================================
# STACK
# Stack is a linked list where:
# - push adds to head
# - pop removes from head
#
# LIFO:
# Last In First Out
#
# Example:
#
# push(3)
# push(5)
# push(9)
#
# 9 <- first removed
# ============================================================
class Stack:

    def __init__(self):
        self.head = None

    def push(self, data):
        # Add node to the front
        self.head = Node(data, self.head)

    def pop(self):
        # Remove node from the front
        if self.head is None:
            return None

        value = self.head.data
        self.head = self.head.next

        return value

    def empty(self):
        return self.head is None

# ============================================================
# QUEUE
#
# Queue uses:
# - head: remove from front
# - tail: add at the end
#
# FIFO:
# First In First Out
#
# Example:
#
# enqueue(3)
# enqueue(5)
# enqueue(9)
#
# 3 <- first removed
# ============================================================
class Queue:

    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data):
        # Create a new node at the tail
        new_node = Node(data)

        # Empty queue
        if self.tail is None:
            self.head = new_node
            self.tail = new_node

        else:
            # Link old tail to new node
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        # Remove from the head
        if self.head is None:
            return None

        value = self.head.data
        self.head = self.head.next

        # Queue became empty
        if self.head is None:
            self.tail = None

        return value

    def empty(self):
        return self.head is None

# ============================================================
# Demonstration -> how it works
# ============================================================
if __name__ == "__main__":

    print("LINKED LIST")
    print("----------------")

    linked = LinkedList()

    # Add nodes like the C++ example:
    # head = new Node(value, head)

    linked.add_front(3)
    linked.add_front(5)
    linked.add_front(9)
    linked.add_front(8)

    # Output: 8 9 5 3
    linked.display()


    print("\nREMOVE HEAD")
    print("----------------")

    removed = linked.remove_front()

    print("Removed:", removed)

    # Output: 9 5 3
    linked.display()

    print("\nSTACK")
    print("----------------")

    stack = Stack()

    stack.push(3)
    stack.push(5)
    stack.push(9)
    stack.push(8)

    # Removes 8 first
    print("Pop:", stack.pop())

    while not stack.empty():
        print(stack.pop(), end=" ")

    print()

    print("\nQUEUE")
    print("----------------")

    queue = Queue()

    queue.enqueue(3)
    queue.enqueue(5)
    queue.enqueue(9)
    queue.enqueue(8)

    # Removes 3 first
    print("Dequeue:", queue.dequeue())

    while not queue.empty():
        print(queue.dequeue(), end=" ")

    print()

# ============================================================
# Summary:
#
# Linked List:
#   Node -> Node -> Node -> None
#
# Node:
#   Stores data + link to next node
#
# Stack:
#   Add/remove at head
#   LIFO
#
# Queue:
#   Add at tail
#   Remove at head
#   FIFO
#
# Complexity:
#
# Add to head:       O(1)
# Remove from head:  O(1)
# Search/traverse:   O(n)
# ============================================================
