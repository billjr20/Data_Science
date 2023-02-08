import statistics
import random



# test case where the bug arises
# A = [1140, 26825, 30573, 31796, 34673, 49261, 56923, 61938]
# B = [14722, 22166, 23232, 31341, 41107, 45933, 46757, 57513]

# A = [1,2,3,4]
# B = [1,5,6,7]

# AB = sorted(A + B)
# print(AB)
# print((AB[len(AB)//2] + AB[len(AB)//2 - 1]) / 2)
# print("Two Numbers needed: ", AB[len(AB)//2], AB[len(AB)//2 - 1])
# print(statistics.median(AB))
# print(median_sorted_arrays(A,B,0,len(A),0,len(B)))

for mA in range(16,21):
    A_list = []
    B_list = []
    for mB in range(2**mA):
        A_list.append(random.randint(0, 2**16))
        B_list.append(random.randint(0, 2**16))
    
    A_list.sort()
    B_list.sort()
    AB = sorted(A_list + B_list)
    print('Num of elements: ', len(A_list), len(B_list))
    print('Median with no duplicates in generated nums:')
    print('Median of built in union: ', statistics.median(AB))
    print('Median of created union: ', median_sorted_arrays(A_list, B_list, 0, len(A_list), 0, len(B_list)))
    print("")