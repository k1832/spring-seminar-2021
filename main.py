from modules.get_prime import get_n_bit_prime_number
if __name__ == '__main__':
    p = get_n_bit_prime_number(512)
    q = get_n_bit_prime_number(512)
    N = p*q
    print(f"Bit length of N: {str(N.bit_length())}")
    print(N)
