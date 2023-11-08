def vig_encrypt(plaintext, vig_cipher, counter):
    ciphertext = ""

    for char in plaintext:
        vig_key_value = 0

        if char.islower():
            vig_key = vig_cipher[counter]

            if vig_key.islower():
                vig_key_value = ord(vig_key) - ord("a")

            elif vig_key.isupper():
                vig_key_value = ord(vig_key) - ord("A")

            vig_char = chr(((ord(char) - ord("a") + vig_key_value) % 26) + ord("a"))
            counter += 1

        if char.isupper():
            vig_key = vig_cipher[counter]

            if vig_key.islower():
                vig_key_value = ord(vig_key) - ord("a")

            elif vig_key.isupper():
                vig_key_value = ord(vig_key) - ord("A")

            vig_char = chr(((ord(char) - ord("A") + vig_key_value) % 26) + ord("A"))
            counter += 1

        if counter == len(vig_cipher):
            counter = 0

        if not char.isalpha():
            vig_char = char

        ciphertext += vig_char

    return ciphertext

vig_cipher = input ("Choose your secret cipher here! : ")
plaintext = input("Enter your message here! : ")
counter = 0

ciphertext = vig_encrypt(plaintext, vig_cipher, counter)

print ("Encrypted message: " + ciphertext)