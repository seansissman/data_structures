# -*- coding: utf-8 -*-
"""
Created on Tue May 11 21:02:13 2021
@author: seans
linked_list is an attempt to simulate a generic linked list data type.

A linked list is a linear data type that is not contiguous in memory. A linked
list is a collection of nodes, which are composed of two parts: data and pointers.
The first node is tracked as the 'head' and the last node is tracked as the
'tail'.

linked_list does restrict element types, specifically the None type is reserved
to indicate the end of the linked_list. Ie. the last node can point to None. 
If the reference to the head of a linked_list points to None, this indicates 
an empty linked_list.

linked_list functionality and complexity:
    Access head- O(1)
    Access tail- O(1)
    Access middle- O(n)
    Search - O(n)
    Insertion head - O(1)
    Insertion tail - O(1)
    Insertion middle - O(n)
    Deletion head- O(1)
    Deletion tail- O(n) - need to find the new tail
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
        

class LinkedList:
    
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
        
        # Make the new node point to the old head
        new_node.next = self.head
        self.head = new_node
        
        if self.tail == None:
            self.tail = self.head
        
    
    def append(self, new_data):
        """ Insert a new Node to the end of the linked list (new tail) """
        new_node = Node(new_data)
        
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:            
            self.tail.next = new_node
            self.tail = new_node
    
    
    def insert_after(self, previous_node, new_data):
        """ Insert a new Node after an existing Node. """
        if not previous_node:
            raise Exception("Node does not exist!")
        
        new_node = Node(new_data)
        new_node.next = previous_node.next
        previous_node.next = new_node
        
        
    # Deletion methods
    def pull(self):
        """ Remove the head of the linked list. """
        if self.head == None:
            raise Exception("Cannot remove from an empty linked list!")
        self.head = self.head.next
        
        
    def pop(self):
        """ Remove the tail of the linked list. """
        if self.tail == None:
            raise Exception("Cannot remove from an empty linked list!")
        
        cur = self.head
        previous = None
        while(cur.next):
            previous = cur
            cur = cur.next
        cur = None
        self.tail = previous
        self.tail.next = None

        
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
        previous = None
        count=0
        while(count < position):
            previous = cur
            cur = cur.next
            count+=1
        previous.next = cur.next
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
        
        
        
        