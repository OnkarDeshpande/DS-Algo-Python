
#unsorted arr
arr = [53,6,2,8,23,5,33,44]

#sorted arr
#arr = [1,2,4,5,7,9]

#take a key element from index 1, compare it with numbers before it.
#insert it at a place where the value of the key element is greater than the
#element to which it is compared
for i in range(1,len(arr)):
    key_val = arr[i]

    compare_with = i-1
    while compare_with > -1 and arr[compare_with]>key_val:
        arr[compare_with+1] = arr[compare_with]
        compare_with -=1

    arr[compare_with+1] = key_val

print(arr)

#order of growth - O(N^2)


