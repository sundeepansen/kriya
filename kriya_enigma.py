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

def encode_chanda(chanda_text):
    encoded_text = ""
    for pattern in chanda_text.split():
        if pattern in chanda_mapping:
            encoded_text += chanda_mapping[pattern]
    return encoded_text

def decode_chanda(encoded_text):
    decoded_text = ""
    for nucleotide in encoded_text:
        for pattern, code in chanda_mapping.items():
            if nucleotide == code:
                decoded_text += pattern + " "
                break
    return decoded_text

def correct_decryption(decoded_text):
    corrected_text = ""
    for chanda_pattern in decoded_text.split():
        for char, chanda_name in chanda_mapping.items():
            if chanda_name == chanda_pattern:
                corrected_text += char
                break
    return corrected_text


# Example usage
plaintext = "shrIguru charana saroja raja nija manu mukuru sudhAri baranaUM raghubara bimala jasu jo dAyaku phala chAri buddhihIna tanu jAnike sumirauM pavana kumAra bala buddhi bidyA dehu mohiM harahu kalesa bikAra"
print("Plaintext:", plaintext)

ciphertext = encrypt(plaintext)
print("Ciphertext:", ciphertext)

decrypted_text = decrypt(ciphertext)
print("Decrypted Text:", decrypted_text)

chanda_text = "Madhya anusThuppu Ukta Sakvari pratisTha Ukta suprstisTha Sakvari Madhya dhRti abhikRti..."
encoded_text = encode_chanda(chanda_text)
print(f"Encoded text: {encoded_text}")
decoded_text = decode_chanda(encoded_text)
print(f"Decoded text: {decoded_text}")

#correct_text = correct_decryption(ciphertext)
#print(correct_text)