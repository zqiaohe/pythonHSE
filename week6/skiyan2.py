def merge(A, B):
    acur = 0
    bcur = 0
    mark = 0
    C = []
    while acur < len(A) and bcur < len(B):
        if A[acur] < B[bcur]:
            # print(acur, A[acur])
            C.append(A[acur])
            acur += 1
            mark = 0
        else:
            # print(bcur, B[bcur])
            C.append(B[bcur])
            bcur += 1
            mark = 1
    # print ('C = ', C)
    if mark == 1:
        C = C + A[acur:]
        return (' '.join(map(str, C)))
        # print(A[acur:])
    else:
        C = C + B[bcur:]
        return (' '.join(map(str, C)))
        # print(B[bcur:])


A = list(map(int, input().split()))
B = list(map(int, input().split()))
print(merge(A, B))
