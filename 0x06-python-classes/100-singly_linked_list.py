#!/usr/bin/python3
"""Defines classes Node and SinglyLinkedList."""


class Node:
    """
    Represents a node of a singly linked list.

    Attributes:
        __data (int): The data stored in the node.
        __next_node (Node): The reference to the next node in the linked list.
    """

    def __init__(self, data, next_node=None):
        """
        Initializes a new Node instance.

        Args:
            data (int): The data to store in the node.
            next_node (Node): The next node in the linked list.

        Raises:
            TypeError: If data is not an integer or next_node is not a Node or None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getter method to retrieve the data attribute."""
        return self.__data

    @data.setter
    def data(self, value):
        """
        Setter method to set the data attribute.

        Args:
            value (int): The data to set.

        Raises:
            TypeError: If data is not an integer.
        """
        if type(value) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """Getter method to retrieve the next_node attribute."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Setter method to set the next_node attribute.

        Args:
            value (Node): The next_node to set.

        Raises:
            TypeError: If next_node is not a Node or None.
        """
        if value is not None and type(value) is not Node:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """Represents a singly linked list."""

    def __init__(self):
        """Initializes an empty SinglyLinkedList."""
        self.head = None

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted position in the list.

        Args:
            value (int): The value to insert.

        Raises:
            TypeError: If value is not an integer.
        """
        if type(value) is not int:
            raise TypeError("data must be an integer")

        new_node = Node(value)
        if self.head is None or value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
            return

        current = self.head
        while current.next_node is not None and current.next_node.data < value:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        """Returns a string representation of the linked list."""
        result = []
        current = self.head
        while current is not None:
            result.append(str(current.data))
            current = current.next_node
        return "\n".join(result)
