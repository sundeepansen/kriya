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

# Generate the DNA mapping dictionary
dna_mapping = generate_dna_mapping()

# Print the DNA mapping dictionary
for character, dna_sequence in dna_mapping.items():
    print(f"{character}: {dna_sequence}")

