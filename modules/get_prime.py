# reference: https://www.geeksforgeeks.org/how-to-generate-large-prime-numbers-for-rsa-algorithm/
import random
first_primes_list = [
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 
    31, 37, 41, 43, 47, 53, 59, 61, 67,  
    71, 73, 79, 83, 89, 97, 101, 103,  
    107, 109, 113, 127, 131, 137, 139,  
    149, 151, 157, 163, 167, 173, 179,  
    181, 191, 193, 197, 199, 211, 223, 
    227, 229, 233, 239, 241, 251, 257, 
    263, 269, 271, 277, 281, 283, 293, 
    307, 311, 313, 317, 331, 337, 347, 349
]

def get_n_bit_random(n):
    return random.randrange(1<<(n-1),1<<n)

def get_low_level_n_bit_prime(n):
    while True:
        candidate = get_n_bit_random(n)

        for divisor in first_primes_list:
            # √candidate < divisor
            if candidate < divisor**2:
                return candidate
            if candidate % divisor == 0:
                break
        return candidate

def miller_rabin_trials_passed(candidate, number_of_trials=20): 
    # If the candidate passes one trial, the probability of the number being prime is 75%.
    # According to the reference.
    max_division_by_two = 0
    ec = candidate-1
    while ec % 2 == 0: 
        ec >>= 1
        max_division_by_two += 1
    assert(2**max_division_by_two * ec == candidate-1) 

    def trial(round_tester): 
        if pow(round_tester, ec, candidate) == 1: 
            return False
        for i in range(max_division_by_two): 
            if pow(round_tester, 2**i * ec, candidate) == candidate-1: 
                return False
        return True

    for _ in range(number_of_trials): 
        round_tester = random.randrange(2, candidate) 
        if trial(round_tester): 
            return False
    return True

def get_n_bit_prime_number(n):
    while True:
        candidate = get_low_level_n_bit_prime(n)
        if miller_rabin_trials_passed(candidate, 100):
            return candidate
