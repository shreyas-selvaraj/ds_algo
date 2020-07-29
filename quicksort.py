#lomuto and hoare's, lomuto quicker to implement but less effective 
# https://www.youtube.com/watch?v=MZaf_9IZCrc
#implement with median pivot after?
#time complexity for BOTH: average: O(nlog(n)), worst case when list already sorted O(n^2)

def lomuto_partition(arr, low, high): #partitions array based on where pivot is placed in array
	pivot = arr[high]
	i = low - 1
	j = low
	while(j < high):
		if arr[j] < arr[high]:
			i = i + 1
			temp = arr[i]
			arr[i] = arr[j]
			arr[j] = temp 
		j = j + 1
	temp = arr[high]
	arr[high] = arr[i + 1]
	arr[i + 1] = temp
	return i + 1

def lomuto_quicksort(arr, low, high):
	if(low < high): 
		partition_index = lomuto_partition(arr, low, high)
		lomuto_quicksort(arr, partition_index + 1, high)
		lomuto_quicksort(arr, low, partition_index - 1)

def hoare_partition(arr, low, high):
	pivot = arr[low]
	i = low - 1
	j = high + 1
	
	while(True): #ensures that i and j keep getting incremented 
		i = i + 1
		while(arr[i] < pivot):
			i = i + 1

		j = j - 1
		while(arr[j] > pivot):
			j = j - 1

		if(i >= j):
			return j

		temp = arr[j]
		arr[j] = arr[i]
		arr[i] = temp


def hoare_quicksort(arr, low, high):
	if(low < high):
		partition_index = hoare_partition(arr, low, high)
		hoare_quicksort(arr, partition_index + 1, high)
		hoare_quicksort(arr, low, partition_index)


arr = [7,2,1,8, 6, 3, 5, 4]
#lomuto_quicksort(arr, 0, len(arr) - 1)
hoare_quicksort(arr, 0, len(arr) - 1)
print(arr)