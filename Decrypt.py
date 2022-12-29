def caesar_decrypt(ciphertext, shift):
  # Create a string to store the decrypted message
  plaintext = ""

  # Loop through each character in the ciphertext
  for ch in ciphertext:
    # Shift the character back by the specified number of positions
    shifted_ch = chr((ord(ch) - shift - 65) % 26 + 65)
    # Add the shifted character to the plaintext
    plaintext += shifted_ch

  # Return the decrypted message
  return plaintext
