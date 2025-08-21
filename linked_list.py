
"""Recursive singly-linked list utility functions and Node class."""

__author__ = "730572401"


class Node:
    """Node in a singly-linked list recursive structure."""
    value: int
    next: "Node | None"

    def __init__(self, value: int, next: "Node | None"):
        """Construct a singly-linked list Node with a value and next Node."""
        self.value = value
        self.next = next

    def __str__(self) -> str:
        """Produce a string representation of the linked list starting at this Node."""
        if self.next is None:
            return f"{self.value} -> None"
        else:
            return f"{self.value} -> {self.next}"


def value_at(head: Node | None, index: int) -> int:
    """Return the value of the Node at the given index. Raise IndexError if out of bounds."""
    if head is None:
        raise IndexError("Index is out of bounds on the list.")
    if index == 0:
        return head.value
    return value_at(head.next, index - 1)


def max(head: Node | None) -> int:
    """Return the maximum value in the linked list. Raise ValueError if the list is empty."""
    if head is None:
        raise ValueError("Cannot call max with None")
    if head.next is None:
        return head.value
    max_rest = max(head.next)
    return head.value if head.value > max_rest else max_rest


def linkify(items: list[int]) -> Node | None:
    """Convert a list of integers into a linked list of Nodes with the same values in order."""
    if len(items) == 0:
        return None
    return Node(items[0], linkify(items[1:]))


def scale(head: Node | None, factor: int) -> Node | None:
    """Return a new linked list where each value is multiplied by the given scaling factor."""
    if head is None:
        return None
    return Node(head.value * factor, scale(head.next, factor))