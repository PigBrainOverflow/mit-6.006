def build_string(T, k):
    char_count = [0 for _ in range(26)]
    D, i = {}, 0
    for j, c in enumerate(T):
        char_count[ord(c) - ord('a')] += 1
        if i < k:
            i += 1
        else:
            char_count[ord(T[j - k]) - ord('a')] -= 1
            if tuple(char_count) in D:
                D[tuple(char_count)] += 1
            else:
                D[tuple(char_count)] = 1
    return D


def count_characters(S):
    char_count = [0 for _ in range(26)]
    for c in S:
        char_count[ord(c) - ord('a')] += 1
    return tuple(char_count)


def count_anagram_substrings(T, S):
    '''
    Input:  T | String
            S | Tuple of strings S_i of equal length k < |T|
    Output: A | Tuple of integers a_i:
              | the anagram substring count of S_i in T
    '''
    A = []
    k = len(S[0])
    D = build_string(T, k)
    for s in S:
        A.append(D.get(count_characters(s), 0))
    return tuple(A)

