1st: LRU Cache:

explanation: 

Effciency:

Space Complexity:

O(n) where n is the capacity of the cache. This is because when the cache is full, least recent used element 
will be deleted.

Time Complexity:

All operations are of O(1) since the cache is implemented by OrderedDict.

Design Choice:
I use OrderedDict to make the code look more compact and elegant. The put method might be a 
little different from the requirement but I believe it is more reasonable to perform an 
"use operation" when the key is already in the cache and we update its value

2nd: File Recursion:


explanation: 

Effciency:

Space Complexity:

1. O(m) where m refers to the maximum depth of a file in the orginal directory. This is because when using
recursion, we determine the space by the longest stream of active stack frames.


Time Complexity:

1. O(n) where n refers to total number of possible paths in the directory. This is because we need to check all
possible paths, which means we need to go through every possible directory, sub-directory, file, etc.

Design Choice:

Simple Recursion and conditional checking.


3rd: HuffmanCoding:

explanation: 

Effciency:

Space Complexity:

obvious O(n) since we need to store each character in the string in a tree.

Time Complexity:

1. The encoding process takes O(nlogn), heapify takes O(n), during each iteration in the loop it takes O(logn) for heappush, 
and it takes n iterations. The DFS takes approximately O(n) where n is the number of characters in the string, which are the leaves
in the tree. The while loop dominate the asymptotic terms, giving O(nlogn).

2. The decoding process takes approximately O(n) where n is the number of characters in the string, which are the leaves
in the tree. This is because the sum of nodes before the leaf level is approximately the number of leaves, giving O(2n)=O(n).


Design Choice:
I use a heap for maintaining minimum elements, and design a treeNode class for storing data for encoding and decoding.



4th Active Directory

explanation: 

Effciency: 

Space Complexity:

O(m) where n is the maximum depth in the recursive tree.

This is because recursion takes call stack space.

Time Complexity:

O(n+m) where n is all the possible users in the current group, including users in the sub-group, 
and m is the number of subgroups in worst case scenario.
This is because we have to check all possibilities to make sure the user is in or not. This constructs
a recursive tree that requires O(n+m)

Design Choice: Recursion that check each user and its sub-group if not found.


5th Blockchain:

explanation: 

Effciency: 

Space Complexity：

O(n) this is straight forward since there are n objects in the Blockchain.

Time Complexity:

Adding Block operation is O(1), assuming the hash calculation operates at O(1). This is because
all operations in block creation takes constant time.


Design Choice: Design Block with prev and next, making it easy to reference as a doubly linkedList. 
The Blockchain class integrates the blocks together.

6th Union & Intersection:

explanation: 

Effciency: Sacrificing a little space leads to linear solutions. 

Space Complexity O(n+m), 

where n is number of unique elements in first linkedlist and m is the number of unique elements in the second
linkedlist. This is because union aggregating the total unique values of two linkedlists.

Time Complexity O(n+m) for both union and intersection,

where n is number of unique elements in first linkedlist and m is the number of unique elements in the second
linkedlist. 

This is because we have to check each element in each linkedlist to see whether it is in the other one or not.


Design Choice: use set data structure for its O(1) and ease of intersection and union.
