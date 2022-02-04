'''
You can use Google Translate with Python.
If you want to make translation mod, it will be very useful for you.
(You can use DeepL as well, but I don't explain about it here.)

ExerciseA Translation

    Translate the list of Japanese strings to English.
    And print each string.

    When you run this program, you have to see the following messages.

    this is a pen.
    test
    I was able to translate!

    Notes
        You need to install googletrans library to use Google Translate.
        like this.

        pip install googletrans==3.1.0a0

        Make sure you installed version 3.1.0a0.
        Other versions have some problems.
'''

from googletrans import Translator

translator = Translator()

text_list=['これはペンです。', 'テスト', '翻訳できたよ！']

#Write code here