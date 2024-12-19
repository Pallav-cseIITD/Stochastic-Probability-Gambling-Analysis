"""
Use the following function to convert the decimal fraction of k/N into it's binary representation
using k_prec number of bits after the decimal point. You may assume that the expansion of 
k/N terminates before k_prec bits after the decimal point.
"""
def decimalToBinary(num, k_prec) : 
  
    binary = ""  
    Integral = int(num)    
    fractional = num - Integral 
   
    while (Integral) :       
        rem = Integral % 2
        binary += str(rem);  
        Integral //= 2

    binary = binary[ : : -1]  
    binary += '.'

    while (k_prec) : 
        fractional *= 2
        fract_bit = int(fractional)  
  
        if (fract_bit == 1) :  
            fractional -= fract_bit  
            binary += '1'       
        else : 
            binary += '0'
        k_prec -= 1
        
    return binary 

def win_probability(p, q, k, N):
    def helper(temp, dic):
        if temp == 0:
            return 0 
        if temp >= N:
            return 1 
        if temp == N / 3:
            return (p**2)/ (1 - p*q)
        if temp in dic:
            return dic[temp]

        if temp < N / 2:
            dic[temp] = p * helper(2 * temp, dic)
        else:
            dic[temp] = p + q * helper(2 * temp - N, dic)
        return dic[temp]
    
    return helper(k, {})

def game_duration(p, q, k, N):
    def helper(temp, dic):
        if temp == 0:
            return 0
        if temp >= N:
            return 0
        if temp == N / 3:
            return (1+p)/ (1 - p*q)
        if temp in dic:
            return dic[temp]
        if temp < N / 2:
            dic[temp] = 1 + p * helper(2 * temp, dic)
        else:
            dic[temp] = 1 + q * helper(2 * temp - N, dic)
        return dic[temp]

    return helper(k, {})
