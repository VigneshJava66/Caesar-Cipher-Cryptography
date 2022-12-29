def caesar_encrypt(plaintext, shift):
  # Create a string to store the encrypted message
  ciphertext = ""

  # Loop through each character in the plaintext
  for ch in plaintext:
    # Shift the character by the specified number of positions
    shifted_ch = chr((ord(ch) + shift - 65) % 26 + 65)
    # Add the shifted character to the ciphertext
    ciphertext += shifted_ch

  # Return the encrypted message
  return ciphertext
