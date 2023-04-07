#!/usr/bin/python3
"""Prime Game"""


def primes(n):
    """
    A helper function that returns a list of prime
    numbers between 1 and n (inclusive).
    """
    primes_list = []
    sieve = [True] * (n + 1)
    for p in range(2, n + 1):
        if sieve[p]:
            primes_list.append(p)
            for i in range(p*p, n + 1, p):
                sieve[i] = False
    return primes_list


def isWinner(x, nums):
    """
    Returns winner of Prime Game.
    Args:
        x (int): number of rounds
        nums (list): upper limit of range
    Return:
        Name of winner or None if winner cannot be found
    """
    if x is None or nums is None or x == 0 or nums == []:
        return None
    maria_count = ben_count = 0
    for i in range(x):
        prime_list = primes(nums[i])
        if len(prime_list) % 2 == 0:
            ben_count += 1
        else:
            maria_count += 1
    if maria_count > ben_count:
        return 'Maria'
    elif ben_count > maria_count:
        return 'Ben'
    else:
        return None
