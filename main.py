def caesar(text, shift, encrypt=True):
    if not isinstance(text, str):
        return "The text should be string"
    if not isinstance(shift, (int)):
        return "The shif should be an integer value"
    if shift<1 or shift>25:
        return "the shift should be between 1 and 25"
    
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    if not encrypt:
        shift = - shift
    

    shifted_alphabets = alphabets[shift:] + alphabets[:shift]
    translation_table = str.maketrans(alphabets + alphabets.upper(), shifted_alphabets + shifted_alphabets.upper())
    encrypted_text = text.translate(translation_table)
    return encrypted_text

def caesar_encrypt(text, shift):
    return caesar(text, shift, True)

def caeser_decrypt(text, shift):
    return caesar(text, shift, False)

encrypt_text = caesar_encrypt("Dishant", 3)
decrypt_text = caeser_decrypt("Glvkdqw", 3)
print(encrypt_text)
print(decrypt_text)