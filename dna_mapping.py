from kriya_enigma import decoded_text


def generate_dna_mapping():
    dna_mapping = {}

    min_ascii = 0
    max_ascii = 127

    for i in range(min_ascii, max_ascii):
        character = chr(i)
        dna_sequence = ""

        # Convert ASCII character to binary
        binary = bin(i)[2:].zfill(7)

        # Map binary digits to DNA bases
        for bit in binary:
            if bit == '0':
                dna_sequence += 'A'
            else:
                dna_sequence += 'T'

        dna_mapping[character] = dna_sequence

    return dna_mapping


def encode_to_dna(text):
    # Generate the DNA mapping dictionary
    dna_mapping = generate_dna_mapping()

    encoded_dna = ""
    for char in text:
        # Check if the character exists in the DNA mapping
        if char in dna_mapping:
            encoded_dna += dna_mapping[char]
        else:
            # Handle characters not in the DNA mapping
            encoded_dna += "N"

    return encoded_dna

def decode_from_dna(encoded_dna):
    # Generate the DNA mapping dictionary
    dna_mapping = generate_dna_mapping()

    decoded_text = ""
    for i in range(0, len(encoded_dna), 7):
        dna_sequence = encoded_dna[i:i+7]
        found = False

        for char, dna in dna_mapping.items():
            if dna == dna_sequence:
                decoded_text += char
                found = True
                break

        if not found:
            # Handle unknown DNA sequences
            decoded_text += "?"

    return decoded_text

#decoded_text = decode_from_dna(encoded_text)

# Example usage
input_text = "Chanda Encryption is a novel encryption scheme that leverages the rhythmic patterns and structures of the Chanda system, derived from Sanskrit poetry, to encrypt and decrypt messages. This white paper presents the concept and implementation of Chanda Encryption, demonstrating its application as a linguistic-based encryption technique. We explore the encryption process, the security considerations, and potential use cases for Chanda Encryption. While Chanda Encryption offers an innovative approach to encryption, it is essential to note that it is primarily intended for educational and experimental purposes rather than stringent security requirements."
# Generate the DNA mapping dictionary
dna_mapping = generate_dna_mapping()

# Encode the input text to DNA
encoded_text = encode_to_dna(input_text)

# Decode the encoded DNA back to text
decoded_text = decode_from_dna(encoded_text)

print("Input Text:", input_text)
print("Encoded DNA:", encoded_text)
print("Decoded Text:", decoded_text)