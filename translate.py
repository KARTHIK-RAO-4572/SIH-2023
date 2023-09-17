#pip install translate

from translate import Translator

def translate_to_telugu(text):
    try:
        translator = Translator(to_lang="te")  # "te" is the ISO code for Telugu
        telugu_translation = translator.translate(text)
        return telugu_translation
    except Exception as e:
        return f"Translation Error: {str(e)}"

# Example usage:
english_text = input("enter words to translate:")
telugu_text = translate_to_telugu(english_text)
print(f"English: {english_text}")
print(f"Telugu: {telugu_text}")