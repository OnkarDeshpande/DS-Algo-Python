#quicksort
import random

def arrange_array(var_arr,left_pointer,pivot_index):
    count = 0
    while count < pivot_index - left_pointer:
        if var_arr[left_pointer+count] > var_arr[pivot_index]:
            var_arr.insert(pivot_index+1,var_arr[left_pointer+count])
            del var_arr[left_pointer+count]
            count -= 1
            pivot_index-=1
        count+=1
    return var_arr,pivot_index

def quicksort(var_arr,left_pointer,right_pointer):
    if len(var_arr[left_pointer:right_pointer])>1:
        pivot_index = right_pointer-1
        var_arr,pivot_index = arrange_array(var_arr, left_pointer, pivot_index)
        quicksort(var_arr,left_pointer,pivot_index)
        quicksort(var_arr,pivot_index+1,right_pointer)
    return var_arr


arr = random.sample(range(50000),10)

sorted_arr = quicksort(arr,0,len(arr))
print(quicksort(sorted_arr,0,len(sorted_arr)))
