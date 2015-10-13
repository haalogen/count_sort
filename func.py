import numpy as np



def my_hash(item, num_buckets):
    return (item % num_buckets)



def count_sort(array, num_buckets):
    count = np.zeros(num_buckets)
    
#    calculate the histogram of key frequencies
    for x in array:
        count[my_hash(x, num_buckets)] += 1
    
    
    total = 0
    for i in range(num_buckets):
        old_count = count[i]
        count[i] = total
        total += old_count
    
    output = np.zeros(array.shape, array.dtype)
#    copy to output array, preserving order of items with equal keys
    for x in array:
        output[count[my_hash(x, num_buckets)]] = x
        count[my_hash(x, num_buckets)] += 1
    
    return output


def count_collisions(array):
    cnt = 0
    n = len(array)
    current_key = array[0]
    
    for i in range(n-1):    # i = [0 .. N-2]
        
        current_key = array[i]
        if array[i] > array[i+1]:   # incorrectly sorted
            cnt += 1
    
    return cnt


