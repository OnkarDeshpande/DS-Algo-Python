

def merge(arr,left_pointer,mid_pointer,right_pointer):
    left_arr = arr[left_pointer:mid_pointer]
    right_arr = arr[mid_pointer:right_pointer]
    large_number = 9999
    left_arr.append(large_number)
    right_arr.append(large_number)

    left_arr_pointer = right_arr_pointer = 0
    for iteration in range(left_pointer,right_pointer):
        if left_arr[left_arr_pointer] <= right_arr[right_arr_pointer]:
            arr[iteration] = left_arr[left_arr_pointer]
            left_arr_pointer+=1
        else:
            arr[iteration] = right_arr[right_arr_pointer]
            right_arr_pointer+=1
    return  arr

def merge_sort(arr,left_pointer,right_pointer):
    if  len(arr[left_pointer:right_pointer])>1 :
        mid_pointer = (left_pointer+right_pointer)//2
        merge_sort(arr,left_pointer,mid_pointer)
        merge_sort(arr,mid_pointer,right_pointer)
        merge(arr,left_pointer,mid_pointer,right_pointer)
    return arr

unsorted_arr = [5,8,9,12,1,200,3,7]

sorted_arr = merge_sort(unsorted_arr,0,len(unsorted_arr))
print(sorted_arr)
