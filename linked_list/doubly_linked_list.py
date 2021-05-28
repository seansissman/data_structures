# -*- coding: utf-8 -*-
"""
Created on Thur May 27 09:30 2021
@author: seans
doubly_linked_list is an attempt to simulate a generic doubly linked list 
data type.

A doubly linked list is a linear data type that is not contiguous in memory. 
A double linked list is the structured the same as a single linked list 
(see linked_list.py) but with each Node containing an additional pointer to the
previous Node. 
The first node is tracked as the 'head' and the last node is tracked as the
'tail'.

doubly_linked_list does restrict element types, specifically the None type is 
reserved to indicate the end of the doubly_linked_list. Ie. the last node can 
point to None. If the reference to the head of a linked_list points to None, 
this indicates an empty doubly_linked_list.

linked_list functionality and complexity:
    Access head- O(1)
    Access tail- O(1)
    Access middle- O(n)
    Search - O(n)
    Insertion head - O(1)
    Insertion tail - O(1)
    Insertion middle - O(n)
    Deletion head- O(1)
    Deletion tail- O(1) - This is an improvement from singly linked lists
    Deletion middle- O(n)
    Determine length - O(n) - need to count each Node

"""


class Node:
    """ Nodes are the elements of the linked list. A node houses a value, and
        a pointer to the next Node in the list.
    """
    
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        

class DoublyLinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        
    
    def __repr__(self):
        return "%s(%r)" % (self.__class__, self.__dict__)
    
    def __str__(self):
        if self.head:
            cur = self.head
            printable = "{"
            while(cur):
                if cur.next:
                    printable = printable + str(cur.data) + "<->"
                else:
                    printable = printable + str(cur.data) + "->"
                cur = cur.next
            printable+= "}"
            return printable
        return "None"
    
    def __len__(self):
        count = 0
        cur = self.head
        while cur:
            count+=1
            cur = cur.next
        return count
    
    def __getitem__(self, k):
        """Return Node at index k. """
        if k < 0:
            raise IndexError("Index " + str(k) + " is out of range.")
        index = 0
        cur = self.head
        while cur:
            if index == k:
                return cur
            cur = cur.next
            index+=1
        raise IndexError("Index " + str(k) + " is out of range.")
    
    
    # Insertion methods
    def push(self, new_data):
        """ Insert a new Node to the beginning of the linked list (new head) """
        new_node = Node(new_data)
        
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        
    
    def append(self, new_data):
        """ Insert a new Node to the end of the linked list (new tail) """
        new_node = Node(new_data)
        
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail            
            self.tail.next = new_node
            self.tail = new_node
    
    
    def insert_after(self, previous_node, new_data):
        """ Insert a new Node after an existing Node. """
        if not previous_node:
            raise Exception("Node does not exist!")
        
        new_node = Node(new_data)

        new_node.prev = previous_node
        new_node.next = previous_node.next
        previous_node.next.prev = new_node
        previous_node.next = new_node
                
        
        
    # Deletion methods
    def pull(self):
        """ Remove the head of the linked list. """
        if not self.head:
            raise Exception("Cannot remove from an empty linked list!")
        self.head.next.prev = None
        self.head = self.head.next
        
        
    def pop(self):
        """ Remove the tail of the linked list. """
        if not self.tail:
            raise Exception("Cannot remove from an empty linked list!")
        
        self.tail.prev.next = None            
        self.tail = self.tail.prev

        
    def remove(self, position):
        """ Remove the Node at a position. """
        if position == 0:
            self.pull()
            return
        if position == len(self)-1:
            self.pop()
            return
        if not 0 <= position < len(self):
            raise IndexError("Position out of bounds!")
            
        cur = self.head
        count=0
        while(count < position):
            cur = cur.next
            count+=1
        cur.prev.next = cur.next
        cur.next.prev = cur.prev
        cur = None
            
        
    # Search method
    def search(self, value):
        """Search for Node containing @param value.
            @return index number if found
            @return -1 if not found
        """
        cur = self.head
        count=0
        while(cur):
            if cur.data == value:
                return count
            cur = cur.next
            count+=1
        return -1
        
        
        
        