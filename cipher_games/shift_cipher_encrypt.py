def encrypt(plaintext, shift_key):
    ciphertext = ""

    for char in plaintext:

        if char.isupper():
            char_index = ord(char) - ord("A")
            char_shifted = (char_index + shift_key) % 26 + ord("A")
            char_encrypted = chr(char_shifted)
            ciphertext+= char_encrypted
        
        elif char.islower():
            char_index = ord(char) - ord("a")
            char_shifted = (char_index + shift_key) % 26 + ord("a")
            char_encrypted = chr(char_shifted)
            ciphertext += char_encrypted

        else:
            ciphertext += char

    return ciphertext

plaintext = input("Enter your message here! : ")
shift_key = 10
ciphertext = encrypt(plaintext, shift_key)

print ("Encrypted message: " + ciphertext)