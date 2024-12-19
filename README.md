# Stochastic-Probability-Gambling-Analysis
\# Stochastic Processes Gambling Analysis

This repository contains implementations of various probability and stochastic process problems focused on gambling scenarios and stock price modeling.

\#\# Problem Overview

The assignment explores different variations of the gambler's ruin problem and Markov chain applications in stock price modeling.

\#\# Problems and Solutions

\#\#\# 1. Classical Gambler's Ruin (\`gambler_ruin.py\`)

A gambler bets on coin tosses where:

\- Heads (probability p): Win \$1

\- Tails (probability q = 1-p): Lose \$1

\- Game ends when wealth reaches \$N or \$0

Solutions implemented:

\- Winning probability calculation from initial wealth k

\- Probability of infinite wealth as N approaches infinity

\- Expected number of rounds until game ends

Implementation approach:

\- Used difference equations for probability calculations

\- Implemented dynamic programming for expected rounds

\- Leveraged geometric series for infinite wealth case

\#\#\# 2. Aggressive Betting Strategy (\`aggressive_betting.py\`)

Modified betting strategy where:

\- For wealth k \< N/2: Bet entire amount

\- For wealth k ≥ N/2: Bet only N-k

\- Double or nothing on each bet

Solutions implemented:

\- Winning probability calculation

\- Expected duration of game

Implementation approach:

\- Recursive probability calculations

\- Binary representation of k/N ratio

\- Dynamic programming for expected duration

\#\#\# 3. Cursed Gambler Problem (\`cursed_gambler.py\`)

Gambling with constraints:

\- After reaching wealth m, can't exceed m+W

\- Automatic loss if reaching m+W

\- Stop at wealth t

Solution implemented:

\- Expected number of gambling rounds

\- Modular arithmetic for final answer (mod 10\^9 + 7)

Implementation approach:

\- System of linear equations

\- Matrix operations for solving expected values

\- Modular inverse calculations

\#\#\# 4. Stock Price Markov Chain (\`stock_price_markov.py\`)

Analysis of stock price movements as a Markov chain:

\- States: {0, 1, 2, ..., N}

\- Price changes by at most 1 unit per step

\- Transition probabilities: (pk, rk, qk)

Solutions implemented:

\- Stationary distribution calculation

\- Expected time to reach price b from price a

Implementation approach:

\- Matrix operations for stationary distribution

\- Linear system solving for expected hitting times

\- Efficient sparse matrix operations

\#\# Usage

Each Python file contains functions that solve specific parts of each problem:

\`\`\`python

\# Example for gambler_ruin.py

def winning_probability(k, N, p):

"""Calculate probability of winning given initial wealth k"""

\# Implementation details

def expected_rounds(k, N, p):

"""Calculate expected number of rounds until game ends"""

\# Implementation details

\`\`\`

\#\# Performance Notes

\- All implementations are optimized to run within 10 seconds

\- Efficient matrix operations used where applicable

\- Memory-efficient implementations for large N values

\#\# Requirements

\- Python 3.x

\- NumPy (for matrix operations)

\- SciPy (for sparse matrix calculations)
