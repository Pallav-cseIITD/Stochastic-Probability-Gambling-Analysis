def win_probability(p, q, k, N):
    if p == q:
        return k/N
    else:
        return (1 - ((q / p) ** k)) / (1 - ((q / p) ** N))

def limit_win_probability(p, q, k):
    if p <= 0.5:
        return 0
    else:
        return 1 - ((q/p)**k)

def game_duration(p, q, k, N):
    if p == 0.5:
        return k * (N - k)
    else:
        first = ((1- ((q/p)**k))* N) / ((1- ((q/p)**N))*(p-q))
        second = k / (q-p)
        return first+second
    
