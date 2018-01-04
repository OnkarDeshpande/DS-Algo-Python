##implementing greedy algo to find min number of refills from going to point b from a
## coursera week 3 lect 3


def minrefills(var_arr,L):
    curr_refill = 0
    num_refills = -1

    while curr_refill < len(var_arr)-1:
        last_refill = curr_refill
        while curr_refill < len(var_arr)-1:
            if var_arr[curr_refill+1] - var_arr[last_refill] < L:
                curr_refill+=1
            else:
                break
        if last_refill == curr_refill :
            return "Not possible"
        if curr_refill <= len(var_arr):
            num_refills+=1

    return num_refills

dist_arr = [200,375,550,750,950]

mileage_len = 400

print(minrefills(dist_arr,mileage_len))