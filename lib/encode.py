
#takes text and key parameters and returns encoded text. 
def encode(text, key):
    cipher = make_cipher(key)
    #print(f"cipher : {cipher}")
    ciphertext_chars = []
    for i in text:
        ciphered_char = chr(65 + cipher.index(i))
        ciphertext_chars.append(ciphered_char)

    return "".join(ciphertext_chars)

#takes encrypted text and key parameters and returns decoded text.
def decode(encrypted, key):
    cipher = make_cipher(key)
    print(f"cipher : {cipher}")
    plaintext_chars = []
    for i in encrypted:
        plain_char = cipher[ord(i)- 65]
        plaintext_chars.append(plain_char)

    return "".join(plaintext_chars)

#takes a key and returns a cipher for for encoding and decoding
def make_cipher(key):
    print(f"key: {key}")
    alphabet = [chr(i + 96) for i in range(1, 27)]
    print(f"alphabet {alphabet}")
    cipher_with_duplicates = list(key) + alphabet

    cipher = []
    for i in range(0, len(cipher_with_duplicates)):
        if cipher_with_duplicates[i] not in cipher_with_duplicates[:i]:
            cipher.append(cipher_with_duplicates[i])

    return cipher

# When you run this file, these next lines will show you the expected
# and actual outputs of the functions above.
print(f"""
 Running: encode("theswiftfoxjumpedoverthelazydog", "secretkey")
Expected: EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL
  Actual: {encode('theswiftfoxjumpedoverthelazydog', 'secretkey')}
""")

print(f"""
 Running: decode("EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL", "secretkey")
Expected: theswiftfoxjumpedoverthelazydog
  Actual: {decode('EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL', 'secretkey')}
""")
