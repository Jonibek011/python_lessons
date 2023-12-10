# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 16:51:19 2023

@author: Javohir
"""

from googletrans import Translator
tarjimon = Translator()
matn_uz = "Python-dunyodagi eng mashxur dasturlash tili"
matn_eng = tarjimon.translate(matn_uz)
# print(matn_eng.origin)
# print(matn_eng.text)
# print(matn_eng.src)
# print(matn_eng.dest)

matn_ru = tarjimon.translate(matn_uz, dest='ru')
# print(matn_ru.text)

# msg = "Tarjima uchun biror matn kiriting, to'xtatish uchun 'q' harfini bosing: "

# while True:
#     text = input(msg)
#     if text == 'q':
#         break
#     else:
#         tarjima = tarjimon.translate(text, src='uz', dest = 'en')
#     print(tarjima.text)

import requests
from pprint import pprint
sahifa = "https://kun.uz/news/main"
r = requests.get(sahifa)
# pprint(r.text)
import googletrans

url = "https://api.adviceslip.com/advice"
r = requests.get(url)
advice = r.json()['slip']['advice']
print(advice)

translator = googletrans.Translator()
tarjima = translator.translate(advice, dest = 'uz')
print(tarjima.text)





