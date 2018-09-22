SECTION A

1.	Array is a container which can hold a fix number of items and these items should be of the same type. Most of the data structures make use of arrays to implement their algorithms. An array data structure, or simply an array , is a data structure consisting of a collection of elements (values or variables ), each identified by at least one array index or key.  An array is stored such that the position of each element can be computed from its index tuple by a mathematical formula.


2.	 A linked list is a linear data structure where each element is a separate object. Each element (we will call it a node ) of a list is comprising of two items - the data and a reference to the next node. The last node has a reference to null. The entry point into a linked list is called the head of the list. It should be noted that head is not a separate node, but the reference to the first node. If the list is empty then the head is a null reference. A linked list is a dynamic data structure. The number of nodes in a list is not fixed and can grow and shrink on demand. Any application which has to deal with an unknown number of objects will need to use a linked list.
Types of Linked Lists
i.	A singly linked list 
ii.	A doubly linked list is a list that has two references, one to the next node and another to previous node.
iii.	Circular linked list where last node of the list points back to the first node (or the head) of the list.


3.	 A HashMap (or Dictionary) is a data structure that implements an associative array abstract data type, a structure that can map keys to values. A hash table uses a hash function to compute an index into an array of buckets or slots, from which the desired value can be found.

4.	 A Set is an abstract data type that can store certain values, without any particular order, and no repeated values. It is a computer implementation of the mathematical concept of a finite Set. The Set data structure is usually used to test whether elements belong to set of values. Rather than only containing elements, Sets are more used to perform operations on multiple values at once with methods such as union, intersect, etc…

5.	The major difference between Array and Linked list regards to their structure. Arrays are index based data structure where each element associated with an index. On the other hand, Linked list relies on references where each node consists of the data and the references to the previous and next element. Basically, an array is a set of similar data objects stored in sequential memory locations under a common heading or a variable name while a linked list is a data structure which contains a sequence of the elements where each element is linked to its next element. There are two fields in an element of linked list. One is Data field, and other is link field, Data field contains the actual value to be stored and processed. Furthermore, the link field holds the address of the next data item in the linked list. The address used to access a particular node is known as a pointer. Another significant difference between an array and linked list is that Array has a fixed size and required to be declared prior, but Linked List is not restricted to size and expand and contract during execution.

6.	 Linked lists are preferable over arrays when:

a.	 You need constant-time insertions or deletions from the list (such as in real-time computing where time predictability is absolutely critical)

b.	 You don't know how many items will be in the list. With arrays, you may need to re-declare and copy memory if the array grows too big

c.	 You don't need random access to any elements

d.	 You want to be able to insert items in the middle of the list (such as a priority queue)

Arrays are preferable when:

a.	 You need indexed/random access to elements

b.	 You know the number of elements in the array ahead of time so that you can allocate the correct amount of memory for the array

c.	 You need speed when iterating through all the elements in sequence. You can use pointer math on the array to access each element, whereas you need to look up the node based on the pointer for each element in linked list, which may result in page faults which may result in performance hits.

d.	 Memory is a concern. Filled arrays take up less memory than linked lists. Each element in the array is just the data. Each linked list node requires the data as well as one (or more) pointers to the other elements in the linked list.

SECTION B
SOLUTION TO SIMPLE ARRAY SUMS:

n = int(input().strip()) 
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')] 
       res = sum(arr) 
       print(res)



SOLUTION TO PLUS MINUS PROBLEM:

import sys
from decimal import * 
  

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')] 
  
 
numOfPositives = 0 
numOfNegatives = 0 
numOfZeros = 0 
for integer in arr: 
      if (integer > 0): 
          numOfPositives = numOfPositives + 1  
      elif (integer < 0): 
          numOfNegatives = numOfNegatives + 1 
  
 
      else: 
          numOfZeros = numOfZeros + 1 
  
 
fractionOfPositives = Decimal(numOfPositives) / Decimal(n) 
fractionOfPositivesWithPrecision = format(fractionOfPositives, '.6f') 
print(fractionOfPositivesWithPrecision) 
  
 
fractionOfNegatives = Decimal(numOfNegatives) / Decimal(n) 
fractionOfNegativesWithPrecision = format(fractionOfNegatives, '.6f')
print(fractionOfNegativesWithPrecision) 
  
 
fractionOfZeros = Decimal(numOfZeros) / Decimal(n) 
fractionOfZerosWithPrecision = format(fractionOfZeros, '.6f') 
print(fractionOfZerosWithPrecision)





