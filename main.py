# reference: https://qiita.com/QUANON/items/e7b181dd08f2f0b4fdbe
# reference: https://hnw.hatenablog.com/entry/20140610
from modules.get_prime import get_n_bit_prime_number
from math import gcd

def lcm(p, q):
    '''
    最小公倍数を求める。
    '''
    return (p * q) // gcd(p, q)

def get_inverse(n, m):
    inv_n = n % m
    str_bin_exp = format(m-2, "b")
    for i in range(1, len(str_bin_exp)):
        inv_n = inv_n * inv_n % m
        if str_bin_exp[i] == "1":
            inv_n = inv_n * n % m
    return inv_n

def get_keys(p, q):
    '''
    与えられた 2 つの素数 p, q から秘密鍵と公開鍵を生成する。
    '''
    N = p * q
    L = lcm(p - 1, q - 1)

    for i in range(2, L):
        if gcd(i, L) == 1:
            E = i
            break

    for i in range(2, L):
        if (E * i) % L == 1:
            D = i
            break

    return (E, N), (D, N)


def encrypt(plain_text_bitstream, public_key):
    '''
    ビット列に変換された plain_text を
    公開鍵 public_key を使って暗号化する。
    '''
    E, N = public_key
    cipher_bitstream = [pow(char, E, N) for char in plain_text_bitstream]
    return cipher_bitstream


def decrypt(cipher_bitstream, private_key):
    '''
    秘密鍵 private_key を使って暗号文 cipher_bitstream を復号する。
    '''
    D, N = private_key
    decrypted_bitstream = [pow(i, D, N) for i in cipher_bitstream]
    return decrypted_bitstream

def encode(text):
    '''
    文字列を数字（ビット列）に変換する
    '''
    return [ord(char) for char in text]

def decode(bitstream):
    '''
    ビット列で表された文字列を元に戻す
    '''
    return ''.join(chr(i) for i in bitstream)

def bitstream_to_hex(bitstream):
    '''
    ビット列を16進数表記に変換する
    '''
    return ''.join([format(bit, 'x') for bit in bitstream])

if __name__ == '__main__':
    p = get_n_bit_prime_number(15)
    q = get_n_bit_prime_number(15)
    public_key, private_key = get_keys(p, q)
    plain_text = 'Welcome to ようこそジャパリパーク！'
    plain_text_bitstream = encode(plain_text)
    cipher_bitstream = encrypt(plain_text_bitstream, public_key)
    decrypted_bitstream = decrypt(cipher_bitstream, private_key)
    decrypted_text = decode(decrypted_bitstream)
    print(f'''
秘密鍵: {public_key}
公開鍵: {private_key}

平文:
「{plain_text}」

ビット列：
    平文:
        「{bitstream_to_hex(plain_text_bitstream)}」
    暗号文:
        「{bitstream_to_hex(cipher_bitstream)}」

平文 (復号後):
「{decrypted_text}」
''')
