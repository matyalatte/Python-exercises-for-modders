from googletrans import Translator

translator = Translator()

text_list=['これはペンです。', 'テスト', '翻訳できたよ！']


#solution 1
#Translates the list of texts and prints each text
translated_list = translator.translate(text_list, src='ja', dest='en')
for translated in translated_list:
    print(translated.text)

#solution 2
#For each text, translates and prints it.
for text in text_list:
    translated = translator.translate(text, src='ja', dest='en')
    print(translated.text)