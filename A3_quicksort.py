# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 16:02:59 2020

@author: Anirudh Raghavan
"""
      
def quick_sort(arr,l,r,p):
    
    if len(arr[l:r]) > 1:
    
        if p == 'first':
            pivot = arr[l]
        
        elif p == 'last':
            pivot = arr[r-1]
            
            #swap pivot
            
            swap = arr[l]
            arr[l] = arr[r-1]
            arr[r-1] = arr[l]
        
        elif p == 'median':
            
            m = (l+r-1)//2
    
            median = median_sel(arr[l], arr[m], arr[r-1])[1]
            
            if median == 'l':
                pivot = arr[l]
            elif median == 'r':
                pivot = arr[r-1]
                
                swap = arr[l]
                arr[l] = arr[r-1]
                arr[r-1] = arr[l]
            
            else:
                pivot = arr[m]
                
                swap = arr[l]
                arr[l] = arr[m]
                arr[m] = arr[l]
        
        
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
    
        quick_sort(arr,l,i, p)
        quick_sort(arr,i+1,r,p)





# Test Case

# Driver code to test above 
arr = [10, 100, 110, 5, 13, 7, 6, 15, 1, 2, 3, 9, 0, 1, 2, 85, 20, 0] 

n = len(arr) 

print ("Given array is") 

for i in range(n): 
    print ("%d" %arr[i]), 
  
quick_sort(arr,0,n,'median') 

len(arr[0:n])

print ("\n\nSorted array is") 
for i in range(n): 
    print ("%d" %arr[i]),



a = 50
b = 61
c = 9  

median_sel(a,b,c)[0]

def median_sel(a,b,c):

    if a >= b:
        if b >= c:
            pivot = b
            ind = 'm'
        else:
            if a >= c:
                pivot = c
                ind = 'r'
            else:
                pivot = a
                ind = 'l'
    else:
        if c >= b:
            pivot = b
            ind = 'm'
        else:
            if a >= c:
                pivot = a
                ind = 'l'
            else:
                pivot = c
                ind = 'r'
    
    return pivot, ind




