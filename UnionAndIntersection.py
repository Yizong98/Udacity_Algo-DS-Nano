class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def getSet(llist_1, llist_2):
    elem_first = set()
    # first pass
    curr = llist_1.head
    while curr:
        elem_first.add(curr.value)
        curr = curr.next
    # second pass
    elem_second = set()
    # first pass
    curr = llist_2.head
    while curr:
        elem_second.add(curr.value)
        curr = curr.next
    return elem_first,elem_second

def union(llist_1, llist_2):
    first, second = getSet(llist_1,llist_2)
    return list(first | second)
    

def intersection(llist_1, llist_2):
    first, second = getSet(llist_1,llist_2)
    return list(first & second)


if __name__ == "__main__":
    # Test case 1

    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    element_1 = [3,2,4,35,6,65,6,4,3,21]
    element_2 = [6,32,4,9,6,1,11,21,1]

    for i in element_1:
        linked_list_1.append(i)

    for i in element_2:
        linked_list_2.append(i)

    print (union(linked_list_1,linked_list_2))
    # [32, 65, 2, 35, 3, 4, 6, 1, 9, 11, 21]
    print (intersection(linked_list_1,linked_list_2))
    # [4, 21, 6]

    # Test case 2

    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()

    element_1 = [3,2,4,35,6,65,6,4,3,23]
    element_2 = [1,7,8,9,11,21,1]

    for i in element_1:
        linked_list_3.append(i)

    for i in element_2:
        linked_list_4.append(i)

    print (union(linked_list_3,linked_list_4))
    # [65, 2, 35, 3, 4, 6, 1, 7, 8, 9, 11, 21, 23]
    print (intersection(linked_list_3,linked_list_4))
    # []
    


    # Test case 3

    linked_list_4 = LinkedList()
    linked_list_5 = LinkedList()

    element_1 = ["haha","hehe","kaka",1,2,3]
    element_2 = ["hkhk","haha",2]

    for i in element_1:
        linked_list_4.append(i)

    for i in element_2:
        linked_list_5.append(i)

    print (union(linked_list_4,linked_list_5))
    # ['haha', 1, 2, 3, 'hkhk', 'hehe', 'kaka']
    print (intersection(linked_list_4,linked_list_5))
    # ['haha', 2]


    # Test case 4

    linked_list_5 = LinkedList()
    linked_list_6 = LinkedList()

    element_1 = []
    element_2 = ["hkhk","haha",2]

    for i in element_1:
        linked_list_5.append(i)

    for i in element_2:
        linked_list_6.append(i)

    print (union(linked_list_5,linked_list_6))
    # ["hkhk","haha",2]
    print (intersection(linked_list_5,linked_list_6))
    # []

"""
explanation: 

Effciency: Sacrificing a little space leads to linear solutions. 

Space Complexity O(n+m), 
where n is number of elements in first linkedlist and m is the number of elements in the second
linkedlist.

Time Complexity O(n+m)

Design Choice: use set data structure for its O(1) and ease of intersection and union.
"""




    
