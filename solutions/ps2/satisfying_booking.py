def merge_back(B, t):
    kt, st, tt = t
    if st == tt:    # empty slot
        return
    if B:   # not empty
        kb, sb, tb = B[-1]
        if kb == kt and tb == st:   # can merge with previous
            B[-1] = (kb, sb, tt)
            return
    B.append(t) # cannot merge, just append

def merge_booking_schedules(B1, B2):
    n1, n2 = len(B1), len(B2)
    i, j = 0, 0
    B = []
    while i < n1 and j < n2:
        k1, s1, t1 = B1[i]
        k2, s2, t2 = B2[j]
        if s1 < s2:
            if t1 <= s2:    # disjoint
                merge_back(B, B1[i])
                i += 1
            else:   # not disjoint
                merge_back(B, (k1, s1, s2))
                if t1 < t2:
                    merge_back(B, (k1 + k2, s2, t1))
                    B2[j] = (k2, t1, t2)
                    i += 1
                else:
                    merge_back(B, (k1 + k2, s2, t2))
                    if t1 == t2:
                        i += 1
                    else:
                        B1[i] = (k1, t2, t1)
                    j += 1
        else:
            if t2 <= s1:
                merge_back(B, B2[j])
                j += 1
            else:
                merge_back(B, (k2, s2, s1))
                if t2 < t1:
                    merge_back(B, (k1 + k2, s1, t2))
                    B1[i] = (k1, t2, t1)
                    j += 1
                else:
                    merge_back(B, (k1 + k2, s1, t1))
                    if t1 == t2:
                        j += 1
                    else:
                        B2[j] = (k2, t1, t2)
                    i += 1
    while i < n1:
        merge_back(B, B1[i])
        i += 1
    while j < n2:
        merge_back(B, B2[j])
        j += 1
    return B


def satisfying_booking_helper(R):
    n = len(R)
    if n == 1:
        s, t = R[0]
        return [(1, s, t)]
    mid = n // 2
    left = R[:mid]
    right = R[mid:]
    return merge_booking_schedules(
        satisfying_booking_helper(left),
        satisfying_booking_helper(right)
    )


def satisfying_booking(R):
    '''
    Input:  R | Tuple of |R| talk request tuples (s, t)
    Output: B | Tuple of room booking triples (k, s, t)
              | that is the booking schedule that satisfies R
    '''
    return tuple(satisfying_booking_helper(R))
