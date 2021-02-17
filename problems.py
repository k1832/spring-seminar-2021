# 課題1
def encode(text):
    '''
    文字列を受け取って、その文字列の文字コードの配列を返す
    例:
        入力: 'こんにちは! Welcome to ISE laboratory!'
        返り値: [12371, 12435, 12395, 12385, 12399, 33, 32, 87, 101, 108, 99, 111, 109, 101, ...]
    ヒント:
        一文字ずつ文字コードに変換して配列で返します。
        'Python 文字をUnicodeに' とか検索するといいかも
    '''
    bitstream = []
    for char in text:
        char_code = ord(char)
        bitstream.append(char_code)
    return bitstream

# 課題2
def hex_text_to_integer(hex_text):
    '''
    16進数表記の数字を文字列で受け取って、Pythonで扱える整数型に変換してから返す
    例:
        入力: '10001'
        返り値: 65537
    ヒント:
        単純に10進数で表記された数字（例えば'128'とか）を数字として扱ってもらうのは簡単です。
        ですが、それが16進数だと伝えるにはどうしたらいいでしょうか？
        'Python 16進数 数字に変換' とか検索するといいかも
    '''
    integer_value = 0
    integer_value = int(hex_text, base=16)
    return integer_value

# 課題3
def encrypt(plain_text_bitstream, E, N):
    '''
    平文テキストの文字コードの配列を受け取って、暗号文のビット列（配列）を返す
    例:
        入力:
            plain_text_bitstream: [12371, 12435, 12395, 12385, 12399, 33, 32, 87, 101, 108, 99, 111, 109, 101, ...]
            E: 65537
            N: 128113...
        返り値: [437529995188086217916081018...., ...., ....]
    ヒント:
        1文字ずつ（配列の要素一つずつ）に対してスライドに登場した計算を行います。
    '''
    cipher_bitstream = []
    for bit in plain_text_bitstream:
        cipher_bit = pow(bit, E, N)
        cipher_bitstream.append(cipher_bit)
    return cipher_bitstream

# 課題3
def decrypt(cipher_bitstream, D, N):
    '''
    暗号文のビット列（配列）を受け取って、平文の文字列の文字コードの配列を返す
    例:
        入力:
            cipher_bitstream: [437529995188086217916081018...., ...., ....]
            D: 123589...
            N: 128113...
        返り値: [12371, 12435, 12395, 12385, 12399, 33, 32, 87, 101, 108, 99, 111, 109, 101, ...]
    ヒント:
        1文字ずつ（配列の要素一つずつ）に対してスライドに登場した計算を行います。
    '''
    decrypted_bitstream = []
    for bit in cipher_bitstream:
        decrypted_bit = pow(bit, D, N)
        decrypted_bitstream.append(decrypted_bit)
    return decrypted_bitstream

# 課題3
def decode(bitstream):
    '''
    文字コードの配列を受け取って、文字列を返す
    例:
        入力: [12371, 12435, 12395, 12385, 12399, 33, 32, 87, 101, 108, 99, 111, 109, 101, ...]
        返り値: 'こんにちは! Welcome to ISE laboratory!'
    '''
    char_array = []
    for bit in bitstream:
        char = chr(bit)
        char_array.append(char)
    text = ''.join(char_array)
    return text

# 課題4
def my_pow(base, exponent, mod):
    '''
    baseのexponent乗をmodで割った余りを返します
    Pythonではpow(base, exponent, mod)で同じ値を求められます。
    例:
        入力:
            base: 12371
            exponent: 65537
            mod: 128113...
    '''
    return_value = 1
    bit_length = exponent.bit_length()
    for bit_i in range(bit_length-1, -1, -1):
        return_value = return_value * return_value % mod
        if (exponent >> bit_i) & 1:
            return_value = return_value * base % mod
    return return_value

if __name__ == '__main__':
    # 課題1
    # 文字列を1文字ずつの文字コードの配列に変換してください。
    plain_text = 'こんにちは! Welcome to ISE laboratory!'
    plain_text_bitstream = encode(plain_text)

    # 課題2
    # 16進数表記で与えられた鍵をPythonのコードで扱えるような整数型に変換してください。
    E_text = '10001'
    D_text = 'afff6c77ae5f9447b4d20d7e01d78f188b98c49c0f45816685ba152f69d87488c42f4a096ff3b26d55dd0092187a6dded9898af02ecf01e61c3c0193c9db1c9805051262bab6f5e968bb3894829863fc4688e5ed75434af96846fd67b29c5f395193f99bafaa79680f76c675f51a786f3e0037020b46ec5da921fa458262cccd'
    N_text = 'b6707abc07b9097e0cfd1d3d3da7a078fff1d0055405b85ab2983c631a71cc9290f7ddbb19762f316de4397a6c27b9421dc7738cbc50a55b228d4c77b0dbd8cea7096e803a57a50e8950f3443b49d118bf55c79e51488f771208ac02abb9cbb0c292891a455def0eb1acbf5274152daf443b9453d7ff3469a8520bb77d3bc5a1'
    E = hex_text_to_integer(E_text)
    D = hex_text_to_integer(D_text)
    N = hex_text_to_integer(N_text)

    # 課題3
    # 平文テキストの文字コードの配列を暗号化して、その暗号化データからさらに平文を復号し、
    # その復号された文字コードデータからテキストに戻してください。
    cipher_bitstream = encrypt(plain_text_bitstream, E, N)
    decrypted_bitstream = decrypt(cipher_bitstream, D, N)
    decrypted_text = decode(decrypted_bitstream)

    print(f'''
    平文:
「{plain_text}」

ビット列：
    平文:
        「{plain_text_bitstream[:5]}」
    暗号文:
        「{cipher_bitstream[0]}」

平文 (復号後):
「{decrypted_text}」
''')

    # 課題4（Advanced!!）
    # 以下を計算する関数を左バイナリ法を用いて実装してください
    # base^exponent % mod（baseのexponent乗をmodで割った余り）
    # Pythonでは、pow(base, exponent, mod)で計算できます。
    base = 12371
    exponent = E
    mod = N
    problem4_ans = my_pow(base, exponent, mod)
    # problem4_ans == pow(base, exponent, mod) となるかどうか確かめてみましょう
