def bubble_sort(var_arr):
    var_length = len(var_arr)
    while var_length > 0:

        for i in range(0,var_length-1):
            if var_arr[i] > var_arr[i+1]:
                #if the next element is big, swap
                var_arr[i], var_arr[i+1] = var_arr[i+1], var_arr[i]

        var_length -= 1
    return var_arr


unsorted_arr = [-2,4,3,1,5]

sorted_arr = bubble_sort(unsorted_arr)

print(sorted_arr)