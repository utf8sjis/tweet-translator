import deepl


class deeplAPI():
    def __init__(self, api_key):
        self.translator = deepl.Translator(api_key)

    def translate(self, source_text, target_lang):
        result = self.translator.translate_text(source_text, target_lang=target_lang) 
        translated_text = result.text

        return translated_text
