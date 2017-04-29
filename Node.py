# Taneli Leppanen
# taneli.leppanen@student.tut.fi
# ALgorithms for Engineering Informatics
# Task 2 - Linked List


# Node class that is stored in the LList class. Node stores the data of any type
# and the "pointer" to the next Node (None if the Node is the last one).
class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node
