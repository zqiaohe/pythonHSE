A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = []
for ind, i in enumerate(A):
    for ind_, j in enumerate(B):
        if i <= j:
            C = [i]
            B = B[:ind_] + C + B[ind_:]
            ind_ = +1
            break
    if C[0] != i:
        C = [i]
        B = B + C
print(' '.join(map(str, B)))
