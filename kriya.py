import random

chanda_patterns = {
    1: {'name': 'Ukta', 'letters_per_line': 1, 'sama_vruttams': 2},
    2: {'name': 'atyukta', 'letters_per_line': 2, 'sama_vruttams': 4},
    3: {'name': 'Madhya', 'letters_per_line': 3, 'sama_vruttams': 8},
    4: {'name': 'pratisTha', 'letters_per_line': 4, 'sama_vruttams': 16},
    5: {'name': 'suprstisTha', 'letters_per_line': 5, 'sama_vruttams': 32},
    6: {'name': 'gaayatri', 'letters_per_line': 6, 'sama_vruttams': 64},
    7: {'name': 'ushTikku', 'letters_per_line': 7, 'sama_vruttams': 128},
    8: {'name': 'anusThuppu', 'letters_per_line': 8, 'sama_vruttams': 256},
    9: {'name': 'bRhati', 'letters_per_line': 9, 'sama_vruttams': 512},
    10: {'name': 'paMkti', 'letters_per_line': 10, 'sama_vruttams': 1024},
    11: {'name': 'trishTuppu', 'letters_per_line': 11, 'sama_vruttams': 2048},
    12: {'name': 'jagati', 'letters_per_line': 12, 'sama_vruttams': 4096},
    13: {'name': 'atijagati', 'letters_per_line': 13, 'sama_vruttams': 8192},
    14: {'name': 'Sakvari', 'letters_per_line': 14, 'sama_vruttams': 16384},
    15: {'name': 'atiSakvari', 'letters_per_line': 15, 'sama_vruttams': 32768},
    16: {'name': 'ashTi', 'letters_per_line': 16, 'sama_vruttams': 65536},
    17: {'name': 'atyashTi', 'letters_per_line': 17, 'sama_vruttams': 131072},
    18: {'name': 'dhRti', 'letters_per_line': 18, 'sama_vruttams': 262144},
    19: {'name': 'atidhRti', 'letters_per_line': 19, 'sama_vruttams': 524288},
    20: {'name': 'kRti', 'letters_per_line': 20, 'sama_vruttams': 1048576},
    21: {'name': 'prakRti', 'letters_per_line': 21, 'sama_vruttams': 2097152},
    22: {'name': 'aakRti', 'letters_per_line': 22, 'sama_vruttams': 4194304},
    23: {'name': 'vikRti', 'letters_per_line': 23, 'sama_vruttams': 8388608},
    24: {'name': 'sukRti', 'letters_per_line': 24, 'sama_vruttams': 16777216},
    25: {'name': 'abhikRti', 'letters_per_line': 25, 'sama_vruttams': 33554432},
    26: {'name': 'utkRti', 'letters_per_line': 26, 'sama_vruttams': 67108864}
}

# Vocabulary of Sanskrit words
vocabulary = {
    2: ['ra-ma', 'ka-ma', 'ga-ṇa'],
    3: ['ga-ṇe-śa', 'vi-ṣṇu', 'sū-rya'],
    4: ['śi-va', 'pa-ra-śu-ra-mā', 'kṛṣ-ṇa', 'ma-ya'],
    5: ['śa-ri-ra', 'ma-nu-ṣya', 'śa-śi-śekhara', 'ni-tya'],
    6: ['brah-ma-jñā-na', 'yu-dhi-ṣṭhi-ra', 'vi-śva-vi-dyā-laya', 'ā-ditya'],
    7: ['ā-śi-ṣha-va-da-tta', 'śa-ra-da-pūr-ṇi-ma', 'ni-rā-ya-ṇa'],
    8: ['vi-dyā-śra-ma', 'prī-ty-ar-tham', 'ma-ha-ra-ja'],
    9: ['śrī-ku-ru-pan-ni-dhi', 'gau-ḍa-pūr-ṇi-ma', 'vi-jñā-na-ka-ra'],
    10: ['ā-tman-nir-bha-ra-tayā', 'sa-ra-sa-vi-ta-ma', 'vi-dyā-pī-ṭha'],
    11: ['pa-ri-pūr-ṇa-ta-man-di-ra', 'ya-ja-ña-pu-ra-s-ka-ri', 'gu-ru-ve-nu-gā-na'],
    12: ['ā-na-n-da-ma-yī-ma-ya', 'śrī-pa-ñcha-dṛ-ṣṭi-kā-ri', 'sū-rya-man-da-la-stha'],
    # Add more words with different syllable counts here
}


# Generate a sentence adhering to a Chanda pattern
def generate_sentence(chanda_info):
    letters_per_line = chanda_info['letters_per_line']
    sentence = []
    line = []

    for _ in range(chanda_info['sama_vruttams']):
        word = get_word_with_letter_count(letters_per_line)
        if len(line) + len(word) <= letters_per_line:
            line.append(word)
        else:
            sentence.append(' '.join(line))
            line = [word]

    sentence.append(' '.join(line))
    return '\n'.join(sentence)

# Get words with a specific syllable count
def get_word_with_letter_count(letter_count):
    return vocabulary.get(letter_count, [])

# Generate sentences for all Chanda patterns
def generate_chandas():
    for chanda_number, chanda_info in chanda_patterns.items():
        print('Chanda:', chanda_info['name'])
        sentence = generate_sentence(chanda_info)
        print('Generated Sentence:')
        print(sentence)
        print()

# Example function call
generate_chandas()
