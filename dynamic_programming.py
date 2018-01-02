#DP  CLRS

## Rod-cutting problem

def dp_cut_rod(var_p,var_n):
    var_arr_r = [var_p[0]]+[-999999 for item in range(1,var_n)]
    return memo_cut_rod(var_p,var_n,var_arr_r)

def memo_cut_rod(var_p,var_n,var_arr_r):
    if var_arr_r[var_n-1]>=0:
        return var_arr_r[var_n-1]
    elif var_n ==0:
        var_q = 0
    elif var_n -1 ==0:
        var_q = var_p[0]
    else:
        var_q = -999999
        iter_count = min((var_n+1),(len(var_p)+1))
        for item in range(1,iter_count):
            var_q = max(var_q,var_p[item-1]+memo_cut_rod(var_p,var_n-item,var_arr_r))
        var_arr_r[var_n-1] = var_q
    return var_q


def dp_bottom_up_cut_rod(var_p,var_n):
## first create a dummy array of revenue, it will have n+1 items, r(0) = 0.
## there will be two for loop, one to go from 1 to the required cut length
## other will go to check the max value of p(i)+r(n-i)
## n =0 mot handled

    var_arr_r = [0] + [-999999 for item in range(0,var_n)]
    if var_arr_r[var_n]>=0:
        var_q = var_arr_r[var_n-1]

    else:
        var_q = var_p[0]
        for r_loop in range(1,var_n+1):
            iter_count = min((var_n ), (len(var_p)))
            for item in range(1,iter_count+1):
                var_q = max(var_q, var_p[item-1]+var_arr_r[r_loop-item])
            var_arr_r[r_loop] = var_q
    return var_q

#inputs

length = [1,2,3,4,5,6,7,8,9,10]
price = [1,5,8,9,10,17,17,20,24,30]


for item in range(1,18):
    print(dp_bottom_up_cut_rod(price,item))




for length in range(1,18):
    print(dp_cut_rod(price,length))

