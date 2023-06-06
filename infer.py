# -*- coding: UTF-8 -*-

# import section
import copy

# function definition


def list_move_pop(L):
    for i in range(len(L)-1):
        L[i] = L[i+1]
    L.pop()
    return L


def check_empty(L):
    if L == [0]:
        return True
    elif not any(L):
        return False
    else:
        return True


def print_check_empty(L):
    if check_empty(L):
        return L
    else:
        return "Empty"


def max_list_index(L, index_a, index_b):
    if L[index_a] == 'N':
        return index_a
    elif L[index_b] == 'N':
        return index_b
    elif L[index_a] < L[index_b]:
        return index_b
    elif L[index_a] > L[index_b]:
        return index_a
    else:
        return "Same"


def min_list_index(L, index_a, index_b):
    if L[index_a] == 'N':
        return index_a
    elif L[index_b] == 'N':
        return index_b
    elif L[index_a] < L[index_b]:
        return index_a
    elif L[index_a] > L[index_b]:
        return index_b
    else:
        return "Same"


def k_equal_appx_match(event_para, sig_para, appr_para):
    sig = copy.deepcopy(sig_para)
    sig.insert(0, 'N')
    event = copy.deepcopy(event_para)
    event.insert(0, 'N')
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
            while q > 0 and p > 0:
                if C[p][q] == C[p-1][q-1] and event[p] == sig[q]:
                    p = p-1
                    q = q-1
                    M.append(p)
                elif C[p-1][q] < (C[p][q-1]+1):
                    p = p-1
                else:
                    q = q-1
            L.append(M)
            for j in range(1, n):
                C[i][j] = j
                start = i
    return L


# "nmt" means "no more than"
# This is a simplified edition of k_nmt_appx_match function, the results will be incorrect in some situations
def simplified_k_nmt_appx_match(event_para, sig_para, appr_para):
    event = copy.deepcopy(event_para)
    sig = copy.deepcopy(sig_para)
    m = len(event)
    k = appr_para+1
    L = [[] for i in range(k)]
    for i in range(k):
        L_pre = k_equal_appx_match(event, sig, i)
        for i_reseult in L_pre:
            L[i].append(i_reseult)
            if i_reseult:
                for index in range(i_reseult[-1], i_reseult[0]+1):
                    event[index] = "S"
    return L


def paper_k_nmt_appx_match(event_para, sig_para, appr_para):
    event = copy.deepcopy(event_para)
    sig = copy.deepcopy(sig_para)
    m = len(event)
    k = appr_para+1
    L = [[] for i in range(k)]
    Q = [[0, m-1]]
    for i in range(k):
        T = []
        while Q:
            H = Q[0]
            Q = list_move_pop(Q)
            D_for_match = ['S' for i in range(m)]
            D_for_match[H[0]:H[-1]+1] = event[H[0]:H[-1]+1]
            D = event[H[0]:H[-1]+1]
            D_start_index = H[0]
            D_end_index = H[-1]
            # print("D_for_match to match:", D_for_match)
            L_pre = k_equal_appx_match(D_for_match, sig, i)
            for i_reseult in L_pre:
                if check_empty(i_reseult):
                    L[i].append(i_reseult)
            # print(L[i])
            for L_item in L[i]:
                # print(L_item)
                B_start_index = D_start_index
                B_end_index = L_item[-1]-1
                D_start_index = L_item[0]+1
                D_end_index = H[-1]
                B = D[0:L_item[-1]]
                D_for_match = ['S' for i in range(m)]
                D_for_match[L_item[0]+1::] = D[L_item[0]+1::]
                D = D[L_item[0]+1::]
                # print("D second:", D)
                if B:
                    start = B_start_index
                    end = B_end_index
                    T.append([start, end])
            if D:
                start = D_start_index
                end = D_end_index
                T.append([start, end])
        Q = T
    return L


def act_infer(event_para, sig_seq_para, appr_para):
    event = copy.deepcopy(event_para)
    sig_seq = copy.deepcopy(sig_seq_para)
    k = copy.deepcopy(appr_para)
    amount = len(sig_seq)
    del_cnt = 0
    LU = []
    LUk = []
    LUlen = []
    for i in range(amount):
        L = paper_k_nmt_appx_match(event, sig_seq[i], k)
        # L=simplified_k_nmt_appx_match(event,sig_seq[i],k)
        for i_k in range(len(L)):
            if check_empty(L[i_k]):
                LU.append(i)
                LUk.append(i_k)
                LUlen.append(len(sig_seq[i]))
                break

    # print("Initial result:")
    # for i in range(len(LU)):
    #     print(i, "Detected signature",
    #           LU[i], "with k=", LUk[i], ", the signature length is", LUlen[i], ".")

    for iter_1 in range(len(LU)):
        for iter_2 in range(iter_1+1, len(LU)):
            if LUk[iter_1] != LUk[iter_2]:
                del_inx = max_list_index(LUk, iter_1, iter_2)
                if LUk[iter_1] != 'N' and LUk[iter_2] != 'N':
                    del_cnt += 1
                LU[del_inx] = 'N'
                LUk[del_inx] = 'N'
                LUlen[del_inx] = 'N'
                continue
            elif LUlen[iter_1] != LUlen[iter_2]:
                del_inx = min_list_index(LUlen, iter_1, iter_2)
                if LUlen[iter_1] != 'N' and LUlen[iter_2] != 'N':
                    del_cnt += 1
                LU[del_inx] = 'N'
                LUk[del_inx] = 'N'
                LUlen[del_inx] = 'N'
                continue

    # print(del_cnt, "items are deleted.")
    for i in range(del_cnt):
        LU.remove('N')
        LUk.remove('N')
        LUlen.remove('N')

    # print("Final result:")
    # for i in range(len(LU)):
    #     print(i, "Detected signature",LU[i], "with k=", LUk[i], ", the signature length is", LUlen[i], ".")

    return LU


# test inside the file
if __name__ == '__main__':
    k0 = 0
    k1 = 1
    k2 = 2
    k3 = 3

    event = ['a', 'a', 'b', 'a', 'c', 'a', 'b', 'a', 'a', 'b', 'a', 'b', 'c']
    signature = ['a', 'b', 'a', 'c']

    signature_4 = ['a']
    signature_0 = ['a', 'b', 'a', 'c']
    signature_1 = ['a', 'b', 'a', 'c', 'a', 'b', 'a', 'a']
    signature_2 = ['x', 'x', 'x', 'x']
    signature_3 = ['a', 'e', 'e', 'e']
    test_signature = [signature_4, signature_0,
                      signature_1, signature_2, signature_3, signature_1]
    print(signature)
    event = ['a', 'a', 'b', 'a', 'c', 'a', 'b', 'a', 'a', 'b', 'a', 'b', 'c']
    event_0 = ['a', 'a', 'b', 'a', 'c', 'a', 'b', 'a', 'a', 'b', 'a', 'b', 'c']
    event_1 = ['a', 'a', 'a', 'a', 'a', 'a', 'a']
    event_2 = ['a']

    # L = simplified_k_nmt_appx_match(event, signature, k3)
    # print("simple result:")
    # print(k3)
    # for i in range(len(L)):
    #     print(i, print_check_empty(L[i]))

    # signature=['a']
    # L = paper_k_nmt_appx_match(event, signature, k3)
    # print("paper result:")
    # print(k3)
    # for i in range(len(L)):
    #     print(i, print_check_empty(L[i]))

    LU = act_infer(event, test_signature, k3)
    print(LU)
    if check_empty(LU):
        print("Matched.")
    else:
        print("Not matched.")

    test_signature = [signature_2, signature_2,
                      signature_2, signature_2, signature_2, signature_2]
    LU = act_infer(event, test_signature, k3)
    print(LU)
    if check_empty(LU):
        print("Matched.")
    else:
        print("Not matched.")
