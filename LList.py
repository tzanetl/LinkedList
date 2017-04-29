# Taneli Leppanen
# taneli.leppanen@student.tut.fi
# ALgorithms for Engineering Informatics
# Task 2 - Linked List

# Sources
# 1) https://www.codefellows.org/blog/implementing-a-singly-linked-list-in-python/

from Node import *


# LList is a linked list that contains value for first and the last Node in
# the list and the length of the list. New Nodes must be added with the .add
# command
class LList(object):

    def __init__(self):
        self.first_node = None
        self.last_node = None
        self.length = 0

    # Definition for print(LList)
    def __str__(self):
        node = self.first_node

        out = "["
        for i in range(self.length):
            out += str(node.data)

            if node != self.last_node:
                out += ", "
            else:
                out += "]"

            node = node.next_node

        return out

    # Add a new data node to the list
    def add(self, data):
        new_node = Node(data)
        last_node = self.last_node

        if self.first_node is None:
            self.first_node = new_node
            self.last_node = new_node
            self.length = 1
        else:
            last_node.next_node = new_node
            self.last_node = new_node
            self.length += 1

    # Returns the length of the list
    def size(self):
        return self.length

    # Returns the value of data at index
    # Raises value error and exits if index not in range
    def get(self, pos):
        try:
            if pos >= self.length:
                raise ValueError
            else:
                node = self.first_node

                for i in range(pos):
                    node = node.next_node

                return node.data

        except ValueError:
            print("ValueError: Index not in range")
            raise

    # Looks for find_data in list and returns its position or None
    def find(self, find_data):
        node = self.first_node

        for i in range(self.length):

            if node.data == find_data:
                return i

            node = node.next_node

        return None

    # Removes Node at the index or the last one if the index is not
    # defined. Data of the removed Node is returned. Raises ValueError if index
    # is out of range.
    def remove(self, pos=None):
        try:
            if pos is not None:
                if not isinstance(pos, int):
                    raise TypeError
                elif pos >= self.length:
                    raise ValueError

            current_node = self.first_node
            next_node = current_node.next_node

            if pos is None:

                while True:

                    if next_node == self.last_node:
                        break
                    else:
                        current_node = next_node
                        next_node = current_node.next_node
            else:

                for i in range(pos):
                    current_node = next_node
                    next_node = current_node.next_node

            self.last_node = current_node
            current_node.next_node = None
            self.length -= 1
            return next_node.data

        except ValueError:
            print("ValueError: Index not in range")
            raise
        except TypeError:
            print("TypeError: Index must be type int or None")
            raise
