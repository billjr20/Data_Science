import statistics
import random


def median_sorted_arrays(A, B):
    # Get the length of the two arrays
    lenA, lenB = len(A), len(B)
    
    # Initialize binary search bounds and half length
    imin, imax, half_len = 0, lenA, (lenA + lenB + 1) // 2
    
    # Perform binary search
    while imin <= imax:
        # Calculate the middle indices of the two arrays
        mA = (imin + imax) // 2
        mB = half_len - mA
        print(A,B)
        print(mA, mB)
        
        # Check if the middle index of A is too small
        if mA < lenA and B[mB - 1] > A[mA]:
            imin = mA + 1
        # Check if the middle index of A is too big
        elif mA > 0 and A[mA - 1] > B[mB]:
            imax = mA - 1
        else:
            # Calculate the maximum value of the left half
            if mA == 0: 
                max_of_left = B[mB - 1]
            elif mB == 0: 
                max_of_left = A[mA - 1]
            else: 
                max_of_left = max(A[mA - 1], B[mB - 1])


            # Calculate the minimum value of the right half
            if mA == lenA: 
                min_of_right = B[mB]
            elif mB == lenB: 
                min_of_right = A[mA]
            else: 
                min_of_right = min(A[mA], B[mB])
            
            # Return the average of the max of the left half and the min of the right half
            return (max_of_left + min_of_right) / 2.0

A_list = [3,3,4,6]
B_list = [1,2,9,10]
print(median_sorted_arrays(A_list, B_list))

# for mA in range(2,16):
#     A_list = []
#     B_list = []
#     for mB in range(2**mA):
#         A_list.append(random.randint(0, 2**32))
#         B_list.append(random.randint(0, 2**32))
    
#     A_list.sort()
#     B_list.sort()
#     print('Num of elements: ', len(A_list), len(B_list))
#     print('Median with no duplicates in generated nums:')
#     print('Median of built in union: ', statistics.median(A_list + B_list))
#     print('Median of created union: ', median_sorted_arrays(A_list, B_list))
#     print("")
#     assert statistics.median(A_list + B_list) == median_sorted_arrays(A_list, B_list)



# Old Code
# def median_of_two_sorted_arrays(A, B):
#     # Get the length of the two arrays
#     n = len(A)
#     m = len(B)
    
#     # If the length of either array is 1, return the larger of the two elements
#     if n <= 1:
#         return max(A[0], B[0])
    
#     if m <= 1:
#         return max(A[0], B[0])
    
#     # Get the medians of the two arrays
#     mA = A[n // 2]
#     mB = B[m // 2]
    
#     # If the median of A is less than or equal to the median of B,
#     # recursively find the median of the union of the right half of A and the left half of B
#     if mA <= mB:
#         return median_of_two_sorted_arrays(A[n // 2:], B[:m // 2 + 1])
#     # If the median of A is greater than the median of B,
#     # recursively find the median of the union of the right half of B and the left half of A
#     else:
#         return median_of_two_sorted_arrays(A[:n // 2 + 1], B[m // 2:])
