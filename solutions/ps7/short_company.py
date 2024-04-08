def short_single_company(SP, n, k):
    '''
    Output:
        l | Length of the longest subsequence of decreasing prices
        s | List of a longest subsequence of decreasing prices
    '''
    # sort prices each day
    x = 1
    P = [sorted(list(SP[k * j : k * (j + 1)])) for j in range(n)]

    # dynamic programming
    dp = [[(1, None) for _ in range(k)] for _ in range(n)]  # (length, parent)
    for i in range(n):
        if i > 0:
            cur = 0
            for j in range(k):  # traverse in order
                # find the first cur with the price larger than j
                while cur < k and P[i][j] >= P[i - 1][cur]:
                    cur += 1
                if cur == k:    # no previous day has a price larger than j
                    dp[i][j] = (1, None)
                else:
                    dp[i][j] = (dp[i - 1][cur][0] + 1, (i - 1, cur))
        for j in range(k - 2, -1, -1):  # traverse in reverse order
            if P[i][j] < P[i][j + 1] and dp[i][j][0] < dp[i][j + 1][0] + 1:
                dp[i][j] = (dp[i][j + 1][0] + 1, (i, j + 1))

    # find the longest subsequence
    day, (l, parent) = max(enumerate(row[0] for row in dp), key=lambda x: x[1])
    # reconstruct the longest subsequence
    s = [P[day][0]]
    while parent is not None:
        s.append(P[parent[0]][parent[1]])
        parent = dp[parent[0]][parent[1]][1]

    return l, s[::-1]


def short_company(C, P, n, k):
    '''
    Input:  C | Tuple of s = |C| strings representing names of companies
            P | Tuple of s lists each of size nk representing prices
            n | Number of days of price information
            k | Number of prices in one day
    Output: c | Name of a company with highest shorting value
            S | List containing a longest subsequence of 
              | decreasing prices from c that doesn't skip days
    '''
    ##################
    # YOUR CODE HERE #
    ##################
    max_l, max_c, max_s = 0, None, None
    for i, SP in enumerate(P):
        l, s = short_single_company(SP, n, k)
        if l > max_l:
            max_l, max_c, max_s = l, C[i], s

    return max_c, max_s
