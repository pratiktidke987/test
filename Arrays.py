# arr = [5, 2, 8, 7, 1, 3, 13 ];     
# temp = 0;    
# #Displaying elements of original array    
# print("Elements of original array: ");    
# for i in range(0, len(arr)):    
#   print(arr[i], end=" ");    
# #Sort the array in ascending order    
# for i in range(0, len(arr)):    
#   for j in range(i+1, len(arr)):    
#     if(arr[i] > arr[j]):    
#       temp = arr[i];    
#       arr[i] = arr[j];    
#       arr[j] = temp;    
# print();    
# #Displaying elements of the array after sorting    
# print("Elements of array sorted in ascending order: ");    
# for i in range(0, len(arr)):    
#   print(arr[i], end=" "); 
# from array import*
# arr = array('i',[])
# n = int(input("Enter the length of array"))
# for i in range(n):
#   x=int(input("Enter the array element "))
#   arr.append(x)

# print(arr)

# val = int(input("Enter the value for search "))
# k=0
# for e in arr:
#   if e==val:
#     print(k)
#     break

# k+=1

# arr.clear()
# print(arr)

from numpy import *

m1=matrix('1 2 3; 4 5 6; 3 6 8')
m2=matrix('1 2 3; 6 4 8; 5 2 9')

m3=m1 * m2;
print(m3)


