from indic_transliteration import sanscript

def sanskrit_to_english(sanskrit_text):
    english_text = sanscript.transliterate(sanskrit_text, sanscript.DEVANAGARI, sanscript.ITRANS)
    return english_text

# Example usage
sanskrit_text = "जय हनुमान ज्ञान गुन सागर जय कपीस तिहुं लोक उजागर रामदूत अतुलित बल धामा अंजनि पुत्र पवनसुत नामा"
print("Sanskrit Text:", sanskrit_text)

english_text = sanskrit_to_english(sanskrit_text)
print("English Transliteration:", english_text)
