def find_vigenere_key(ciphertext, plaintext):
    key_stream = [(ord(c) - ord(p)) % 26 for c, p in zip(ciphertext, plaintext)]
    key_chars = ''.join(chr(k + ord('A')) for k in key_stream)

    for key_len in range(2, len(key_chars) + 1):
        if key_chars[:key_len] == key_chars[key_len:2 * key_len]:
            return key_chars[:key_len]

    return key_chars


ciphertext = input().strip()
plaintext = input().strip()

print(find_vigenere_key(ciphertext, plaintext))
