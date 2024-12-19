def stationary_distribution(p, q, r, N):
    ans = [1] * (N + 1)
    for k in range(1, N + 1):
        ans[k] = (p[k - 1] * ans[k - 1]) / q[k]
    sum = 0
    for k in ans:
        sum += k

    ans = [item /sum for item in ans]
    return ans

def expected_wealth(p, q, r, N):
    ans = stationary_distribution(p,q,r,N)
    sum = 0
    for i in range(len(ans)):
        sum += i*ans[i]
    return sum
    
def expected_time(p, q, r, N, a, b):
    mat1 = [[0] * (N + 1) for i in range(N + 1)]
    mat2 = [1] * (N + 1)
    mat2[b] = 0
    for k in range(N + 1):
        if k == b:
            mat1[k][k] = 1
        else:
            mat1[k][k] = 1 - r[k]
            if k > 0: mat1[k][k - 1] = -q[k]
            if k < N: mat1[k][k + 1] = -p[k]
    for i in range(N + 1):
        temp = mat1[i][i]
        mat1[i] = [item / temp for item in mat1[i]]
        mat2[i] = mat2[i]/temp
        for j in range(i + 1, N + 1):
            temp = mat1[j][i]
            mat1[j] = [mat1[j][k] - temp * mat1[i][k] for k in range(N + 1)]
            mat2[j] -= temp * mat2[i]
    
    x = [0] * (N + 1)
    for i in range(b, a-1,-1):
        x[i] = mat2[i] - sum(mat1[i][j] * x[j] for j in range(i + 1, N + 1))
    return x[a]