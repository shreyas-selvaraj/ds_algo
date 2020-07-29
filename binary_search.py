'''Tree - A Tree is an undirected, connected, acyclic graph
A Binary Tree is a tree data structure in which each node has at most two children, which are referred to as the left child and right child
Full Tree: a tree in which every node has either 0 or 2 children
Perfect Binary Tree: a binary tree in which all interior nodes have two children and all leave have the same depth
Complete Tree: a binary tree in which every level except possibly the last is full and all nodes in the last level are as far left as possible
'''

'''
Binary Search Tree:
type of binary tree which maintains the property that the value in each node must be greater 
than or equal to any value stored in the left sub-tree, and less than or equal 
to any value stored in the right sub-tree
'''

#construction binary search tree
class Node:
	def __init__(self, left = None, right = None, val = None):
		self.left = left
		self.right = right
		self.val = val

class BST:
	def __init__(self, root):
		self.root = root

	def printTree(self, node): #three traversal methods preorder(root, left, right), inorder(left, root, right), postorder
		#using inorder traversal to get things in order 
		if(node == None):
			return 
		self.printTree(node.left)
		print(node.val)
		print("END LEFT")
		self.printTree(node.right)
		print("END RIGHT")

	def minNode(self, node):
		while(node.left != None):
			node = node.left
		return node



	def insert(self, val):
		#assumes there is a root from construction
		curr = self.root
		while(curr != None): #continue until u find empty node to insert in 
			if val < curr.val:
				if(curr.left == None):
					curr.left = Node(val = val)
					break
				else:
					curr = curr.left
			else: #how to handle duplicates 
				if(curr.right == None):
					curr.right = Node(val = val)
					break
				else:
					curr = curr.right

	def remove(self, val):
		##assume value is in tree
		curr = self.root
		side = ""
		while(curr.val != val):
			temp = curr #node before value is found 
			if(val < curr.val):
				curr = curr.left
				side = "left"
			else:
				curr = curr.right
				side = "right"

		#reassignment of nodes: #make min of left side point to beginning of right side 
		minimum = self.minNode(temp)
		minimum.left = None
		minimum.right = curr.right
		del curr
		if side == "right":
			#assignment points to same object in python
			temp.right = minimum
		else:
			temp.left = minimum
		print("Finished")

	def binarySearch(self, node, val):
		#assumes val is in tree
		#assume tree is sorted as well 
		if node == None or node.val == val:
			return node

		if val < node.val:
			return bst.binarySearch(node.left, val)

		else:
			return bst.binarySearch(node.right, val)


bst = BST(Node(val = 8))
bst.insert(3)
bst.insert(10)
bst.insert(1)
bst.insert(6)
bst.insert(14)
bst.insert(4)
bst.insert(7)
bst.insert(13)
#print(bst.root.left.left.val)
#bst.printTree(bst.root)
#print(bst.minNode(bst.root).val)
#bst.remove(1)
#bst.printTree(bst.root)
print(bst.binarySearch(bst.root, 1))

'''time complexities:
log base 2 of n, but dont care about base 
access: average: O(log(n)), worst: O(n)
search: average: O(log(n)), worst: O(n)
insert: average: O(log(n)), worst: O(n)
delete: average: O(log(n)), worst: O(n)
'''































