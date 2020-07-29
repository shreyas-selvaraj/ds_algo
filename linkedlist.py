#Linked List singly linked + associated methods with time complexities:

#construction
class Node:
	def __init__(self, dataval = None): 
	#dataval None sets default value to null, 
	#allows to have construction with or without parameter
		self.dataval = dataval
		self.next = None

class SLinkedList:
	def __init__(self, head = None):
		self.head = head

head = Node("S")
list1 = SLinkedList(head)
e2 = Node("H")
e3 = Node("R")
head.next = e2
e2.next = e3

#access some number node, average: O(n/2 -> n), worst: O(n) 
def accessNthNode(n):
#cant iterate using for in loop, assumes value exists 
	currNode = list1.head
	for i in range(0, n):
		currNode = currNode.next

	return currNode.dataval

#search for some value, average: O(n/2 -> n), worst: O(n)
def findVal(val):
	counter = 0;
	currNode = list1.head
	while currNode != None:
		if currNode.dataval == val:
			break
		else:
			counter = counter + 1
			currNode = currNode.next

	if currNode == None:
		return "Element not in list"
	return counter

#insertion, average: O(1) because you insert at front or O(1 at back if you have a tail pointer, worst: O(1)
def headInsert(val):
	temp = list1.head
	list1.head = Node(val)
	list1.head.next = temp

def tailInsert(val):
	currNode = head
 	while currNode.next != None:
 		currNode = currNode.next
 	currNode.next = Node(val)

#deletion, average and worst same as insertion for same reason

#Linked List doubly linked:
#access: average: O(n), worst: O(n)
#search: average: O(n), worst: O(n)
#insertion: average: O(1), worst: O(1)
#deletion: average: O(1), worst: O(1)

#Linked List circular: 
#same as above 