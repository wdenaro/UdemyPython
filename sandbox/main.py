# Inspired by https://www.geeksforgeeks.org/convert-text-speech-python/

from gtts import gTTS

import os

mytext = "Situata tra Milano e Verona, Brescia, Capitale Italiana della Cultura 2023, è una città \
        che ha tanto da offrire. In primis, ha una storia antica, come testimonia la sua origine: \
        la Brixia romana, posta lungo la via Gallica, era tra le città più importanti dell’Italia \
        settentrionale. Se vi state chiedendo cosa vedere a Brescia in un giorno, sappiate che i \
        posti da visitare sono tantissimi. Siete pronti?"
language = 'it'

mytext = "The path of the righteous man is beset on all sides by the iniquities of the selfish and the tyranny of\
        evil men. Blessed is he who, in the name of charity and good will, shepherds the weak through the valley of\
        darkness, for he is truly his brother’s keeper and the finder of lost children. And I will strike down upon\
        thee with great vengeance and furious anger those who would attempt to poison and destroy My brothers. And you\
        will know My name is the Lord when I lay My vengeance upon thee."

language = 'en'

myobj = gTTS(text=mytext, lang=language, slow=False)

myobj.save('samuel_l.mp3')

# os.system('afplay welcome.mp3')
