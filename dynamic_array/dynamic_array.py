# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 13:53:50 2021
dynamic_array is an attempt to simulate a generic dynamic array data type.

Dynamic arrays can grow and shrink in size. Can implement with a static array
with an initial capacity. If capacity is exceeded, then create a new static
arry with double the capacity, and copy original array + new element into 
the new array.

dynamic_array does not restrict element type. Ie. can mix int, bool, String, etc.

dynamic arrayrray functionality and complexity:
    Access - O(1)
    Search - O(n)
    Insertion - O(n)
    Appending - O(1)
    Deletion - O(n)
    
@author: seans
"""

class DynamicArray(object):
    """"DynamicArray class"""

    def __init__(self, count=0):
        """Default count and capacity to 0
           @param count defaults to 0 if none provided                                
        """
        # Count of elements in the array
        self.count = count

        # Capacity (max number of elements) of array
        self.capacity = count
        
        # Array object
        self.A = self.initialize_array()
        
        
        
    # Needed to define an immutable container
    def __len__(self):
        """@return the number of elements in the array"""
        return self.count
    
    
    def __getitem__(self, k):
        """Return element at index k
           Provides access functionality 
        """
        if not 0 <= k <= self.count:
            raise IndexError("Index " + str(k) + " is out of range.")
        return self.A[k]
    
    
    
    # DynamicArray methods
    def initialize_array(self):
        """@return an array of None elements of size capacity"""
        return [None for each in range(self.capacity)]
    
    
    def search(self, value):
        """Search the array for the provided value.
           @param value = search value
           @return index of the first occurrence of value. Else return -1
        """
        for i in range(self.count):
            if value == self.A[i]:
                return i
        return -1
    
    
    def insert(self, pos, value):
        """Insert a value into the array at a specified position.
           @param pos = position in which to insert the value
           @param value = value to insert
        """
        # If pos is > array size (count) then append the value
        if pos < 0:
            raise IndexError("Index cannot be less than 0.")
        elif pos >= self.count:
            raise IndexError("Index cannout be greater than array length.")
        else:    
            self.A[pos] = value
                
        
    def append(self, value):
        """Appends the value to the end of the array.
           If capacity is exceeded (count > capacity), double the capacity size.
        """
        if self.count >= self.capacity:
            if self.capacity == 0:
                self.capacity = 1
            else:
                self.capacity*=2
        self.count+=1
        
        # Emulate allocating new memory 
        temp_arr = self.A + [value]
        self.A = temp_arr


    def delete(self, value):
        """Removes the first occurrence of a value from the array.
           After a removal, shifts the array to fill the blank index.
        """
        for i in range(self.count):
            if self.A[i] == value:
                front = self.A[:i]
                back = self.A[i+1:]
                self.A = front + back
                break
        else:
            raise ValueError("Value " + value + " does not exist in array.")
        
    
    def find(self, value):
        """Returns the index of the first occurrence of a value.
           Returns -1 if the value is not found.
        """
        for i in range(self.count):
            if self.A[i] == value:
                return i
        return -1
            
    
