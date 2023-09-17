#pip install googletrans==4.0.0-rc1

from googletrans import Translator

# Create a Translator object
translator = Translator()

# Text to translate
text_to_translate = input("enter english words: ")

# Translate from English to Telugu
translated_text = translator.translate(text_to_translate, src='en', dest='te')

# Print the translated text
print(translated_text.text)