# #!/usr/bin/python3


# def is_prime(num):
#     """
#     A helper function that returns True if num is prime, False otherwise.
#     """
#     if num < 2:
#         return False
#     for i in range(2, int(num**0.5)+1):
#         if num % i == 0:
#             return False
#     return True


# def isWinner(x, nums):
#     """
#     Determines winner of Prime Game
#     Args:
#         x (int): no. of rounds of game
#         nums (int): upper limit of range for each round
#     Return:
#         Name of winner (Maria or Ben) or None if winner cannot be found
#     """
#     if x is None or nums is None or x == 0 or nums == []:
#         return None
#     Maria = Ben = 0
#     for i in range(x):
#         num = nums[i]
#         primes_count = 0
#         for j in range(2, num+1):
#             if is_prime(j) and num % j == 0:
#                 primes_count += 1
#         if primes_count % 2 == 0:
#             Ben += 1
#         else:
#             Maria += 1
#     if Maria > Ben:
#         return 'Maria'
#     elif Ben > Maria:
#         return 'Ben'
#     return None



def primes(n):
    """
    A helper function that returns a list of prime numbers between 1 and n (inclusive).
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
    Determines winner of Prime Game.
    Args:
        x (int): number of rounds of game
        nums (list): upper limit of range for each round
    Return:
        Name of winner (Maria or Ben) or None if winner cannot be found
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
