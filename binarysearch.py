

def binary_search(arr,var_left,var_right,key):
	if var_left>var_right:
		return -1
	mid_val = int((var_left+var_right)/2)

	if arr[mid_val]==key:
		return mid_val
	elif arr[mid_val] < key:
		return binary_search(arr,mid_val+1,var_right,key)
	else:
		return binary_search(arr,var_left-1,mid_val,key)


sorted_arry = [5,6,8,20,45,67]

print(binary_search(sorted_arry,0,len(sorted_arry)-1,20))

