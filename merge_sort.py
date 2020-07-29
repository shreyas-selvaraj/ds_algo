#same time complexity as quicksort with better worst case but takes up more space 
#divide and conquer
'''
Divide and Conquer is an algorithmic paradigm. A typical Divide and Conquer algorithm solves a problem using following three steps.

Divide: Break the given problem into subproblems of same type.
Conquer: Recursively solve these subproblems
Combine: Appropriately combine the answers
'''

def merge_sort(values): 
  
    if len(values)>1: 
        m = len(values)//2
        left = values[:m] 
        right = values[m:] 
        left = merge_sort(left) 
        right = merge_sort(right) 
  
        values =[] 
  
        while len(left)>0 and len(right)>0: 
            if left[0]<right[0]: 
                values.append(left[0]) 
                left.pop(0) 
            else: 
                values.append(right[0]) 
                right.pop(0) 
  
        for i in left: 
            values.append(i) 
        for i in right: 
            values.append(i) 
                  
    return values

arr = [7,2,1,8, 6, 3, 5, 4]
#lomuto_quicksort(arr, 0, len(arr) - 1)
print(merge_sort(arr))

#time complexity: average and worst: O(nlog(n))
