encrypted_message = caesar_encrypt("HELLO WORLD", 3)
print(encrypted_message) # Output: "KHOOR ZRUOG"

decrypted_message = caesar_decrypt(encrypted_message, 3)
print(decrypted_message) # Output: "HELLO WORLD"
