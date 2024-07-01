#!/usr/bin/python3
"""Prime game file"""


def isWinner(x, nums):
    """is a winner function"""
    def sieve(n):
        """Generate list of primes up to n using the Sieve of Eratosthenes."""
        is_prime = [True] * (n + 1)
        p = 2
        while (p * p <= n):
            if (is_prime[p] == True):
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False
            p += 1
        primes = [p for p in range(2, n + 1) if is_prime[p]]
        return primes

    max_n = max(nums)
    primes_up_to_max_n = sieve(max_n)

    def play_game(n):
        """Simulate the game and determine the winner for a given n."""
        remaining = set(range(1, n + 1))
        primes = [p for p in primes_up_to_max_n if p <= n]
        turn = 0  # 0 for Maria's turn, 1 for Ben's turn
        while primes:
            prime = primes.pop(0)
            multiples = set(range(prime, n + 1, prime))
            remaining -= multiples
            primes = [p for p in primes if p in remaining]
            turn = 1 - turn

        return "Maria" if turn == 1 else "Ben"

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = play_game(n)
        if winner == "Maria":
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
