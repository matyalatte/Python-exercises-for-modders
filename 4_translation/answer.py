from googletrans import Translator

translator = Translator()

text_list=['これはペンです。', 'テスト', '翻訳できたよ！']


#answer 1
#Translate the list of texts and print each text
translated_list = translator.translate(text_list, src='ja', dest='en')
for translated in translated_list:
    print(translated.text)

#answer 2
#For each text, translate and print it.
for text in text_list:
    translated = translator.translate(text, src='ja', dest='en')
    print(translated.text)