from googletrans import Translator

class Google_Translator:
    def __init__(self):
        self.translator = Translator()
        self.result = {'src_text': '', 'src_lang': '', 'tgt_text': '', 'tgt_lang': ''}
 
    def translate(self, text, lang='en'):
        translated = self.translator.translate(text, dest=lang)
        self.result['src_text'] = translated.origin
        self.result['src_lang'] = translated.src
        self.result['tgt_text'] = translated.text
        self.result['tgt_lang'] = translated.dest
 
        return self.result
 
    def translate_file(self, file_path, lang='en'):
        with open(file_path, 'r') as f:
            text = f.read()
        return self.translate(text, lang)

if __name__ == '__main__':
    translator = Google_Translator()

    # Select the option you want to use

    input_text = input('Press Enter to translate: ')
    result = translator.translate(input_text, "ko")

    print('[{}] -> [{}]'.format(result['src_lang'], result['tgt_lang']))
    print('=' * 50)
    print('Source Text : {}'.format(result['src_text']))
    print('Target Text : {}'.format(result['tgt_text']))