import numpy as np
"""
Use the following functions to add, multiply and divide, taking care of the modulo operation.
Use mod_add to add two numbers taking modulo 1000000007. ex : c=a+b --> c=mod_add(a,b)
Use mod_multiply to multiply two numbers taking modulo 1000000007. ex : c=a*b --> c=mod_multiply(a,b)
Use mod_divide to divide two numbers taking modulo 1000000007. ex : c=a/b --> c=mod_divide(a,b)
"""
M=1000000007

def mod_add(a, b):
    a=(a%M+M)%M
    b=(b%M+M)%M
    return (a+b)%M

def mod_multiply(a, b):
    a=(a%M+M)%M
    b=(b%M+M)%M
    return (a*b)%M

def mod_divide(a, b):
    a=(a%M+M)%M
    b=(b%M+M)%M
    return mod_multiply(a, pow(b, M-2, M))

def game_duration(p, q, k, t, W):
    N = k+W+1-t
    k -= t
    t = 0 #reference for others
    
    x = (N+1)**2  #square because for each wealth from 0 to N, we have min wealth W to W+N 
    mat = np.zeros((x, x))

    #I am taking i = wealth and j = min wealth
    for i in range(N+1):
        for j in range(i+1):
            curr = i*(N+1) + j
            
            if i == 0:
                mat[curr][curr] = 1
                continue
                
            if i > 0: #loss
                temp = min(j, i - 1)
                newcurr = (i - 1) * (N + 1) + temp
                mat[curr][newcurr] = q
            #win
            if i + 1 <= j + W and i + 1 <= N:
                newcurr = (i + 1) * (N + 1) + j
                mat[curr][newcurr] = p
            else:
                newcurr = (i - 1) * (N + 1) + j
                mat[curr][newcurr] += p

    checker = []
    for i in range(1, N+1):
        for j in range(i+1):
            checker.append(i*(N+1) +j)
    
    submat = mat[np.ix_(checker, checker)]   #using to check for each case
    iden = np.eye(len(checker))   #identity matrix
    invmat = np.linalg.inv(iden - submat) #inverse matrix
    rhs = np.ones((len(checker), 1))

    time = np.dot(invmat, rhs)
    req = checker.index(k*(N+1) + k)
    
    return time[req][0]
