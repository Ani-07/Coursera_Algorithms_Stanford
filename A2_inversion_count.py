# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 14:37:56 2020

@author: Anirudh Raghavan
"""

def merge(arr, l, m, r): 
    inv_count = 0
    n1 = m - l + 1
    n2 = r - m 
  
    # create temp arrays 
    L = [0] * (n1) 
    R = [0] * (n2) 
  
    # Copy data to temp arrays L[] and R[] 
    for i in range(0 , n1): 
        L[i] = arr[l + i] 
  
    for j in range(0 , n2): 
        R[j] = arr[m + 1 + j] 
  
    # Merge the temp arrays back into arr[l..r] 
    i = 0     # Initial index of first subarray 
    j = 0     # Initial index of second subarray 
    k = l     # Initial index of merged subarray 
  
    while i < n1 and j < n2 : 
        if L[i] <= R[j]: 
            arr[k] = L[i] 
            i += 1
        else: 
            inv_count += 1
            arr[k] = R[j] 
            j += 1
        k += 1
  
    # Copy the remaining elements of L[], if there 
    # are any
    while i < n1: 
        arr[k] = L[i]
        i += 1
        k += 1
  
    # Copy the remaining elements of R[], if there 
    # are any 
    while j < n2: 
        arr[k] = R[j] 
        j += 1
        k += 1
        inv_count += 1
    
    print(inv_count)
        
    return inv_count
  
# l is for left index and r is right index of the 
# sub-array of arr to be sorted 

def mergeSort(arr,l,r): 
    
    print(l,r)    
    
    
    # Same as (l+r)//2, but avoids overflow for 
    # large l and h 
    m = (l+r)//2
        
    print(m)
    
    if l < m: 
  
  
        # Sort first and second halves 
        inv_l = mergeSort(arr, l, m) 
        print(m+2)
    
    if m < r:
        
        inv_r = mergeSort(arr, m+1, r) 
        print(m+2)
    inv_tot = merge(arr, l, m, r) 
        
    inv_count = inv_l + inv_r + inv_tot
        
    return inv_count
  
# Driver code to test above 
arr = [12, 11, 5, 13, 7, 6, 15, 1, 2, 3, 9, 0] 
n = len(arr) 
print ("Given array is") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
a = mergeSort(arr,0,n-1) 
print ("\n\nSorted array is") 
for i in range(n): 
    print ("%d" %arr[i]),
    