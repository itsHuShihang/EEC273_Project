# -*- coding: UTF-8 -*-


import copy


event = ['a', 'a', 'b', 'a', 'c', 'a', 'b', 'a', 'a', 'b', 'a', 'b', 'c']
event_1 = ['a', 'a', 'b', 'a', 'c', 'a', 'b', 'a', 'a', 'b', 'a', 'b', 'c']
signature = ['a', 'b', 'a', 'c']

activities = [[] for i in range(21)]
# print(activities)
activities[0] = event_1
# print(activities)


def list_move_pop(L):
    for i in range(len(L)-1):
        L[i] = L[i+1]
    L.pop()
    return L


def print_check_empty(L):
    if L == []:
        return "Empty!"
    else:
        return L

def k_equal_appx_match(event_para, sig_para, appr_para):
    sig=copy.deepcopy(sig_para)
    sig.insert(0, 'N')
    event=copy.deepcopy(event_para)
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
            while q > 0 and p>0:
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

# nmt means no more than
# def paper_k_nmt_appx_match(event_para, sig_para, appr_para):
#     event=copy.deepcopy(event_para)
#     sig=copy.deepcopy(sig_para)
#     m = len(event)
#     k = appr_para+1
#     L = [[] for i in range(k)]
#     Q = [[0, m-1]]
#     for i in range(k):
#         T = []
#         while Q:
#             H = Q[0]
#             Q = list_move_pop(Q)
#             D = event[H[0]:H[-1]+1]
#             D_start_index = H[0]
#             D_end_index = H[-1]
#             print("D is",D)
#             L_pre=k_equal_appx_match(D,sig,i)
#             for i_reseult in L_pre:
#                 L[i].append(i_reseult)
#             print("L is ", L)
#             print("i is",i)
#             print("Li is",L[i])
#             for L_item in L[i]:
#                 B_start_index = H[0]
#                 print("item -1 is", L_item[-1])
#                 B_end_index = L_item[-1]-1
#                 D_start_index = L_item[0]+1
#                 D_end_index = H[-1]
#                 B = D[0:L_item[-1]]
#                 D = D[L_item[0]+1::]
#                 if B:
#                     start = B_start_index
#                     end = B_end_index
#                     T.append([start, end])
#             if D:
#                 start = D_start_index
#                 end = D_end_index
#                 T.append([start, end])
#         Q = T
#     return L

# "nmt" means "no more than"
def k_nmt_appx_match(event_para, sig_para, appr_para):
    event=copy.deepcopy(event_para)
    sig=copy.deepcopy(sig_para)
    m = len(event)
    k = appr_para+1
    L = [[] for i in range(k)]
    for i in range(k):
        L_pre=k_equal_appx_match(event,sig,i)
        for i_reseult in L_pre:
            L[i].append(i_reseult)
            for index in range(i_reseult[-1],i_reseult[0]+1):
                event[index]="S"
    return L

def act_infer(event, sig, appr_para):
    return 0


if __name__ == '__main__':
    k0 = 0
    k1 = 1
    k2 = 2
    k3 = 3

    L=k_nmt_appx_match(event,signature,k3)
    for i in range(len(L)):
        print(i,print_check_empty(L[i]))

    # L=paper_k_nmt_appx_match(event,signature,k3)
    # print("test result is")
    # for i in range(len(L)):
    #     print(i,print_check_empty(L[i]))