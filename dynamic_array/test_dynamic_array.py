# -*- coding: utf-8 -*-
"""
Unit testing for dynamic_array
Created on Tue May  4 08:58:13 2021

@author: seans
"""
import unittest
from dynamic_array.dynamic_array import DynamicArray

class DynamicArrayTestCase(unittest.TestCase):
    def setUp(self):
        self.da2size = 6
        
        self.da1 = DynamicArray()
        
        self.da2 = DynamicArray(self.da2size)
        self.da2.insert(0,0)
        self.da2.insert(1,'hi there')
        self.da2.insert(2,'see ya')
        self.da2.insert(3,'hi again')
        self.da2.insert(5,0)
        
        
    def test_da_size(self):
        self.assertEqual(len(self.da1), 0)
        self.assertEqual(len(self.da2), self.da2size) 
       
        
    def test_da_getitem(self):
        #Test no indexes in da1
        with self.assertRaises(IndexError):
            self.da1[0]
            
        #Test indexes exist in da2
        self.assertEqual(self.da2[0], 0)
        self.assertEqual(self.da2[1], 'hi there')
        #should be None at -2
        self.assertIsNone(self.da2[len(self.da2)-2])
        
        #Test index larger than array size will fail
        with self.assertRaises(IndexError):
            self.da2[len(self.da2)]
            
        #Test negative index will fail (unlike most Python iterators)
        with self.assertRaises(IndexError):
            self.da2[-1]
    
            
    def test_insert(self):
        #Test cannot insert into empty array
        with self.assertRaises(IndexError):
            self.da1.insert(0,0)
        
        #Test inserting into non-empty array
        self.da2.insert(0,99)
        self.assertEqual(self.da2[0],99)

        
        self.da2.insert(self.da2size-2,'hi')
        self.assertEqual(self.da2[self.da2size-2],'hi')

        
        #Test cannot insert out of bounds for non-empty array
        with self.assertRaises(IndexError):
            self.da1.insert(-1,0)
        with self.assertRaises(IndexError):
            self.da1.insert(10,0)
        

    def test_append(self):
        #Test appending
        self.da2.append(999)
        self.assertEqual(self.da2[len(self.da2)-1], 999)
        self.da2.append('take two')
        self.assertEqual(self.da2[len(self.da2)-1], 'take two')
        a = [0,'hi there','see ya','hi again',None,0,999,'take two']
        dalist = [each for each in self.da2]
        self.assertListEqual(a, dalist)
        
        #Test appending into an empty array
        self.da1.append(1234)
        self.assertEqual(self.da1[0],1234)
        
        
    def test_delete(self):
        #Test attempt to delete value that does not exist in the array
        with self.assertRaises(ValueError):
            self.da2.delete('nothing')

        #Test attempt to delete partial string value
        with self.assertRaises(ValueError):
            self.da2.delete('hi')

        #Test attempt to delete partial string
        with self.assertRaises(ValueError):
            self.da2.delete('hi')
            
        #Test deleting element that is in the array once  
        self.da2.delete('see ya')
        self.assertEqual([each for each in self.da2],[0, 'hi there', 'hi again', None, 0])

        #Test deleting element that is in the array twice        
        self.da2.delete(0)
        self.assertEqual([each for each in self.da2],['hi there', 'hi again', None, 0])

    
    def test_find(self):
        #Test failure to find item in the array
        self.assertEqual(self.da2.find('?'),-1)
        
        #Test failure to find item with partial match
        self.assertEqual(self.da2.find('hi'), -1)
        
        #Test finding item in the array once
        self.assertEqual(self.da2.find('hi again'),3)
        
        #Test finding item in the array multiple times
        self.assertEqual(self.da2.find(0),0)
        
    

if __name__ == '__main__':
    unittest.main()