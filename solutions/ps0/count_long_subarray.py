def count_long_subarray(A):
    '''
    Input:  A     | Python Tuple of positive integers
    Output: count | number of longest increasing subarrays of A
    '''
    count, max_len, cur_len = 0, 0, 1
    n = len(A)
    for i in range(0, n - 1):
        if A[i] < A[i + 1]:
            cur_len += 1
            if cur_len == max_len:
                count += 1
            if cur_len > max_len:
                count, max_len = 1, cur_len
        else:
            cur_len = 1

    return count
