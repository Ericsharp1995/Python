def decrypt(ciphertext, shift_key):
    decrypted_plaintext = ""

    for char in ciphertext:
        if char.isupper():
            char_index = ord(char) - ord("A")
            char_unshifted = (char_index - shift_key) % 26 + ord("A")
            char_decrypted = chr(char_unshifted)
            decrypted_plaintext += char_decrypted

        elif char.islower():
            char_index = ord(char) - ord("a")
            char_unshifted = (char_index - shift_key) % 26 + ord("a")
            char_decrypted = chr(char_unshifted)
            decrypted_plaintext += char_decrypted

        else:
            decrypted_plaintext += char

    return decrypted_plaintext


ciphertext = input("Enter yout encrypted message here! : ")
shift_key = 10
decrypted_plaintext = decrypt(ciphertext, shift_key)

print ("Decrypted message: " + decrypted_plaintext)