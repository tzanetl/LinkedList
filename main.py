# Taneli Leppanen
# ALgorithms for Engineering Informatics
# Task 2 - Linked List

# Sources
# 1) https://www.codefellows.org/blog/implementing-a-singly-linked-list-in-python/


from LList import *


def main():

    l1 = LList()
    l1.add(2)
    l1.add(5)
    l1.add(7)
    l1.add(91)
    l1.add(8)
    print(l1.remove(8))
    print(l1)
    print(l1.size())


main()
