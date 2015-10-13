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
    num_buckets_range = range(1, NUM_BUCKETS+1)
    print num_buckets_range
    num_collisions = np.zeros(NUM_BUCKETS+1, dtype=int)
    
    for num_buckets in num_buckets_range:
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
    
    
    
#    plotting collision graph
    fig_collis = plt.figure()
    ax_collis = fig_collis.add_subplot(111)
    ax_collis.plot(num_buckets_range, num_collisions[1:],
                        label='collisions')
    collis_title = """
Collision analysis of Counting Sort, N=%r, 
array values in [0, NUM_BUCKETS=%r) """ % (N, NUM_BUCKETS)
    ax_collis.set_title(collis_title)
    ax_collis.set_xlabel('# of buckets')
    ax_collis.set_ylabel('# of incorrectly sorted elements')
    ax_collis.set_ylim([0, N])
    ax_collis.legend()
    
    
#    plotting time(N) graph
    fig_time = plt.figure()
    ax_time = fig_time.add_subplot(111)
    ax_time.plot(len_array_range, time_count_sort_list,
                    label='time', marker='o')
    time_title = """
Time of Counting Sort depending on length of array N"""
    ax_time.set_title(time_title)
    ax_time.set_xlabel('N')
    ax_time.set_ylabel('Time of Counting Sort, sec')
#    ax_time.set_ylim([0, max(time_count_sort_list)*1.2])
    ax_time.legend(loc=2)
    
    
#    plt.show()
    fig_collis.savefig("collis_%r_%r_%r.png" % (N, NUM_BUCKETS, NUM_ITERS))
    fig_time.savefig("time_%r_%r_%r.png" % (N, NUM_BUCKETS, NUM_ITERS))



if __name__ == '__main__':
    main()
