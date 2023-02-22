# Inspired by https://www.geeksforgeeks.org/convert-text-speech-python/

from gtts import gTTS

import os

mytext = "Situata tra Milano e Verona, Brescia, Capitale Italiana della Cultura 2023, è una città \
        che ha tanto da offrire. In primis, ha una storia antica, come testimonia la sua origine: \
        la Brixia romana, posta lungo la via Gallica, era tra le città più importanti dell’Italia \
        settentrionale. Se vi state chiedendo cosa vedere a Brescia in un giorno, sappiate che i \
        posti da visitare sono tantissimi. Siete pronti?"

language = 'it'

myobj = gTTS(text=mytext, lang=language, slow=False)

myobj.save('welcome.mp3')

os.system('afplay welcome.mp3')
