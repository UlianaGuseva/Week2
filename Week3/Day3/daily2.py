from translate import Translator

def translate_french(data):
    translation = {}
    for i in data:
        translator = Translator(from_lang='French', to_lang='English')
        translation[i] = translator.translate(i)
    print(translation)


french_words= ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"] 
translate_french(french_words)