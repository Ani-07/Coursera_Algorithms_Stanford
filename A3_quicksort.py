# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 16:02:59 2020

@author: Anirudh Raghavan
"""
      
def quick_sort(arr,l,r):
    
    if len(arr[l:r]) > 1:
    
        pivot = arr[l]
        
        i = l
        k = l + len(arr[l:r])
        
        for j in range(l+1,k):
            if arr[j] <= pivot:
                i += 1
                swap = arr[i]
                arr[i] = arr[j]
                arr[j] = swap
        swap = arr[i]
        arr[i] = pivot
        arr[l] = swap
        
        print(arr)
        print(i)
        print(arr[l:i])
        print(arr[i+1:r])
    
        quick_sort(arr,l,i)
        quick_sort(arr,i+1,r)


# Test Case

# Driver code to test above 
arr = [10, 100, 110, 5, 13, 7, 6, 15, 1, 2, 3, 9, 0, 1, 2, 85, 20, 0] 

n = len(arr) 

print ("Given array is") 

for i in range(n): 
    print ("%d" %arr[i]), 
  
quick_sort(arr,0,n) 

len(arr[0:n])

print ("\n\nSorted array is") 
for i in range(n): 
    print ("%d" %arr[i]),

    
