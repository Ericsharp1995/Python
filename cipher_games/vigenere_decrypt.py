def vig_decrypt(ciphertext, vig_cipher, counter):
    decrypted_plaintext = ""

    for char in ciphertext:
        vig_key_value = 0

        if char.islower():
            vig_key = vig_cipher[counter]

            if vig_key.islower():
                vig_key_value = ord(vig_key) - ord("a")

            elif vig_key.isupper():
                vig_key_value = ord(vig_key) - ord("A")

            plain_char = chr(((ord(char) - vig_key_value - ord("a")) % 26) + ord("a"))
            counter += 1

        if char.isupper():
            vig_key = vig_cipher[counter]

            if vig_key.islower():
                vig_key_value = ord(vig_key) - ord("a")

            elif vig_key.isupper():
                vig_key_value = ord(vig_key) - ord("A")

            plain_char = chr(((ord(char) - vig_key_value - ord("A")) % 26) + ord("A"))
            counter += 1

        if counter == len(vig_cipher):
            counter = 0

        if not char.isalpha():
            plain_char = char

        decrypted_plaintext += plain_char

    return decrypted_plaintext
    
vig_cipher = input ("Enter the secret cipher here! : ")
ciphertext = input ("Enter the encrypted message here! : ")
counter = 0

decryped_plaintext = vig_decrypt(ciphertext, vig_cipher, counter)

print ("Decrypted message: " + decryped_plaintext)