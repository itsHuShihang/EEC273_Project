# -*- coding: UTF-8 -*-
event = ['a', 'a', 'b', 'a', 'c', 'a', 'b', 'a', 'a', 'b', 'a', 'b', 'c']
signature = ['a', 'b', 'a', 'c']


def k_equal_appx_match(sig, event, appr_para):
    sig.insert(0, 'N')
    event.insert(0, 'N')
    print(sig)
    print(event)
    L = []
    start = 1
    m = len(event)
    n = len(sig)
    C = [[0 for i in range(n)] for j in range(m)]
    for i in range(m):
        C[i][0] = 0
    for j in range(1, n):
        C[0][j] = j
    for i in range(1, m):
        for j in range(1, n):
            if event[i] == sig[j]:
                C[i][j] = C[i-1][j-1]
            elif C[i-1][j] < (C[i][j-1]+1):
                C[i][j] = C[i-1][j]
            else:
                C[i][j] = C[i][j-1]+1
        if j == n-1 and C[i][j] == appr_para:
            M = []
            p = i
            q = j
            while q > 0:
                if C[p][q] == C[p-1][q-1] and event[p] == sig[q]:
                    M.append(p)
                    p = p-1
                    q = q-1
                elif C[p-1][q] < (C[p][q-1]+1):
                    p = p-1
                else:
                    q = q-1
            L.append(M)
            print(C)
            for j in range(1, n):
                C[i][j] = j
                start = i
    return L


def k_nomore_appx_match(sig, event, appr_para):
    return 0


def act_infer(sig, event, appr_para):
    return 0


if __name__ == '__main__':
    k1 = 0
    k2 = 0
    k3 = 0
    L = k_equal_appx_match(signature, event, k1)
    print(L)
