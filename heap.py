'''
A Heap is a specialized tree based structure data structure that satisfies the heap 
property: if A is a parent node of B, then the key (the value) of node A is ordered with 
espect to the key of node B with the same ordering applying across the entire heap. A heap 
can be classified further as either a "max heap" or a "min heap". In a max heap, 
the keys of parent nodes are always greater than or equal to those of the children and 
the highest key is in the root node. In a min heap, the keys of parent nodes are less 
than or equal to those of the children and the lowest key is in the root node

Access max or min: O(1)
Insert: O(log(n))
Remove max/min O(log(n))
'''