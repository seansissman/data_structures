# -*- coding: utf-8 -*-
"""
Unit testing for linked_list
Created on Mon May  24 11:57 2021

@author: seans
"""
import unittest
from linked_list.linked_list import LinkedList

class LinkedListTestCase(unittest.TestCase):
    def setUp(self):
        self.ll1 = LinkedList()
        self.ll1.append(1)
        self.ll1.append(2)
        self.ll1.append('tuna')

        
    def test_len(self):
        self.assertEqual(len(self.ll1), 3)
        
        
    # Test access    
    def test_head_access(self):
        self.assertEqual(self.ll1.head.data, 1)
        self.assertEqual(self.ll1.head.next.data, 2)
        self.assertEqual(self.ll1.head.next.next.data, 'tuna')
        self.assertEqual(self.ll1.head.next.next.next, None)
        
    def test_tail_access(self):
        self.assertEqual(self.ll1.tail.data, 'tuna')
        self.assertEqual(self.ll1.tail.next, None)
        
    def test_index_access(self):
        self.assertEqual(self.ll1[0].data, 1)
        self.assertEqual(self.ll1[1].data, 2)
        self.assertEqual(self.ll1[2].data, 'tuna')
        with self.assertRaises(IndexError):
            self.ll1[-1]
        with self.assertRaises(IndexError):
            self.ll1[8]
        
        
    # Test insertions
    def test_append(self):
        self.ll1.append(5)
        self.assertEqual(self.ll1.tail.data, 5)
        self.assertEqual(self.ll1.tail.next, None)
        # Test on empty linked list
        ll2 = LinkedList()
        ll2.append('test')
        self.assertEqual(ll2.head.data, 'test')
        self.assertEqual(ll2.tail.data, 'test')
        
    def test_push(self):
        self.ll1.push(4)
        self.assertEqual(self.ll1.head.data, 4)
        self.assertEqual(self.ll1.head.next.data, 1)
        self.assertEqual(self.ll1.tail.data, 'tuna')
        # Test on empty linked list
        ll2 = LinkedList()
        ll2.push('test')
        self.assertEqual(ll2.head.data, 'test')
        self.assertEqual(ll2.tail.data, 'test')        
        
    def test_insert_after(self):
        self.ll1.insert_after(self.ll1.head, 'burger')
        self.assertEqual(self.ll1.head.next.data, 'burger')
        with self.assertRaises(Exception):
            self.ll1.insert_after('nothing', 'garbage')
        
        
    # Test deletions
    def test_pull(self):
        self.ll1.pull()
        self.assertEqual(self.ll1.head.data, 2)
        ll2 = LinkedList()
        with self.assertRaises(Exception):
            ll2.pull()
            
    def test_pop(self):
        self.ll1.pop()
        self.assertEqual(self.ll1.tail.data, 2)
        ll2 = LinkedList()
        with self.assertRaises(Exception):
            ll2.pop()
            
    def test_remove(self):
        # Test removing head
        self.ll1.remove(0)
        self.assertEqual(self.ll1.head.data, 2)
        self.assertEqual(self.ll1.tail.data, 'tuna')
        # Test removing tail
        self.ll1.remove(1)
        self.assertEqual(self.ll1.head.data, 2)
        self.assertEqual(self.ll1.tail.data, 2)
        # Rebuild the linked list
        self.ll1.push(11)
        self.ll1.append('big tuna')
        # Test removing from the middle
        self.ll1.remove(1)
        self.assertEqual(self.ll1.head.data, 11)
        self.assertEqual(self.ll1.tail.data, 'big tuna')
        self.assertEqual(self.ll1.head.next.data, 'big tuna')
        # Test removing from an empty linked list
        ll2 = LinkedList()
        with self.assertRaises(IndexError):
            ll2.remove(1)

    # Test search
    def test_search(self):
        self.assertEqual(self.ll1.search(1),0)
        self.assertEqual(self.ll1.search(2),1)
        self.assertEqual(self.ll1.search('tuna'),2)
        self.assertEqual(self.ll1.search('nope'),-1)
        
    

if __name__ == '__main__':
    unittest.main()