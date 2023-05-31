import random

# Mapping table for character to Chanda pattern
chanda_mapping = {
    'A': 'Ukta',
    'B': 'atyukta',
    'C': 'Madhya',
    'D': 'pratisTha',
    'E': 'suprstisTha',
    'F': 'gaayatri',
    'G': 'ushTikku',
    'H': 'anusThuppu',
    'I': 'bRhati',
    'J': 'paMkti',
    'K': 'trishTuppu',
    'L': 'jagati',
    'M': 'atijagati',
    'N': 'Sakvari',
    'O': 'atiSakvari',
    'P': 'ashTi',
    'Q': 'atyashTi',
    'R': 'dhRti',
    'S': 'atidhRti',
    'T': 'kRti',
    'U': 'prakRti',
    'V': 'aakRti',
    'W': 'vikRti',
    'X': 'sukRti',
    'Y': 'abhikRti',
    'Z': 'utkRti',
    'a': 'Ukta',
    'b': 'atyukta',
    'c': 'Madhya',
    'd': 'pratisTha',
    'e': 'suprstisTha',
    'f': 'gaayatri',
    'g': 'ushTikku',
    'h': 'anusThuppu',
    'i': 'bRhati',
    'j': 'paMkti',
    'k': 'trishTuppu',
    'l': 'jagati',
    'm': 'atijagati',
    'n': 'Sakvari',
    'o': 'atiSakvari',
    'p': 'ashTi',
    'q': 'atyashTi',
    'r': 'dhRti',
    's': 'atidhRti',
    't': 'kRti',
    'u': 'prakRti',
    'v': 'aakRti',
    'w': 'vikRti',
    'x': 'sukRti',
    'y': 'abhikRti',
    'z': 'utkRti',
    '0': 'Ukta',
    '1': 'atyukta',
    '2': 'Madhya',
    '3': 'pratisTha',
    '4': 'suprstisTha',
    '5': 'gaayatri',
    '6': 'ushTikku',
    '7': 'anusThuppu',
    '8': 'bRhati',
    '9': 'paMkti',
}

# Encrypt plaintext using Chanda patterns
def encrypt(plaintext):
    ciphertext = ''
    for char in plaintext:
        if char in chanda_mapping:
            chanda_pattern = chanda_mapping[char]
            ciphertext += chanda_pattern + ' '
    return ciphertext.strip()

# Decrypt ciphertext by converting Chanda patterns back to characters
def decrypt(ciphertext):
    plaintext = ''
    chanda_patterns = ciphertext.split()
    for chanda_pattern in chanda_patterns:
        for char, pattern in chanda_mapping.items():
            if pattern == chanda_pattern:
                plaintext += char
    return plaintext

# Example usage
plaintext = "HELLO"
print("Plaintext:", plaintext)

ciphertext = encrypt(plaintext)
print("Ciphertext:", ciphertext)

decrypted_text = decrypt(ciphertext)
print("Decrypted Text:", decrypted_text)
