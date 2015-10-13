"""Analysis of Counting Sort algorithm."""
import func as fu
import sys
import numpy as np
import time
import matplotlib.pyplot as plt


def main():
    N = 10
    NUM_BUCKETS = 5
    NUM_ITERS = 1
    
    if len(sys.argv) >= 4:
        N = int(sys.argv[1])
        NUM_BUCKETS = int(sys.argv[2])
        NUM_ITERS = int(sys.argv[3])
    else:
        print """
Usage: 
    python analysis.py [len_array] [num_buckets] [num_iters]
Ex:
    python analysis.py 10 5 1
"""
        sys.exit(-1)
    
#    create random array a
    a = np.random.randint(0, NUM_BUCKETS, N)
    ctrl_a = np.array(sorted(a))
    print 'Random a: \n', a, '\n'
    print 'Timsorted a: \n', ctrl_a, '\n'
    
    
    # collision analysis
    num_collisions = np.zeros(NUM_BUCKETS+1, dtype=int)
    for num_buckets in range(1, NUM_BUCKETS+1):
        count_a = fu.count_sort(a, num_buckets)
        print "Count_sorted a, NUM_BUCKETS=%r:" % num_buckets
        print count_a
#        count collisions
        num_collisions[num_buckets] = fu.count_collisions(count_a)
        print "NUM_COLLISIONS=%r \n" % num_collisions[num_buckets]
    
    
    
    # time(N) analysis
    len_array_range = range(N//10, N*10, N)
    time_count_sort_list = []
    
    for len_array in len_array_range:
        time_count_sort = 0
        
        for i in range(NUM_ITERS):
            _rand_a = np.random.randint(0, NUM_BUCKETS, len_array)
            
            start = time.time()
            _count_a = fu.count_sort(_rand_a, NUM_BUCKETS)
            time_count_sort += (time.time() - start)
            
            if not all(_count_a == sorted(_rand_a)):
                print "Sorting error! _count_a != sorted(_rand_a)"
                sys.exit(-1)
                
        
        time_count_sort /= NUM_ITERS
        time_count_sort_list.append(time_count_sort)    
        print "time_count_sort, N=%r: %r sec" % (
                            len_array, time_count_sort)
    
    
    
#    PLOTTING
    




if __name__ == '__main__':
    main()
