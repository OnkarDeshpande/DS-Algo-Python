

##pdf is in the mail from drej

##DP assignment 3

def partitions_count(var_num):

    memo_dict ={}

    if var_num in memo_dict:
        return memo_dict[var_num]

    if var_num<=2:
        memo_dict[1] = 1
        memo_dict[2] = 1
        return memo_dict[var_num]
    elif var_num == 3:
        temp =  1 + partitions_count(var_num-1)
    elif var_num == 4:
        temp =  1 + partitions_count(var_num-1) + partitions_count(var_num-3)
    else:
        temp =  partitions_count(var_num-1)
        temp += partitions_count(var_num-3)
        temp += partitions_count(var_num-4)

    memo_dict[var_num] = temp
    return memo_dict[var_num]


def dp_partition_bu(var_num):

    memo_dict = {}
    memo_dict[1]=memo_dict[2] = 1
    memo_dict[3] = 2
    memo_dict[4] = 4

    for item in range(5,var_num+1):
        memo_dict[item] = memo_dict[item-1] + memo_dict[item-3] + memo_dict[item-4]

    return memo_dict[var_num]

# for item in range(1,10):
#     print(dp_partition_bu(item))

# for item in range(1, 10):
#     print(partitions_count(item))

## test case

print(dp_partition_bu(100001))