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


mytext = "Dans la terre de Paris, où les rues sont bordées de croissants et les vélos errent librement, il y avait un chemin pavé qui menait à un lieu mystérieux. On disait que si l'on suivait le chemin assez longtemps, on trouverait un morceau perdu de fromage mûr qui accorderait un bonheur éternel.\
    Un jour, un brave aventurier se mit en route sur son vélo fiable pour trouver le fromage. Il chevaucha sur le chemin pavé, sentant les pierres lisses sous ses roues. Pédalant, il fredonnait une chanson qu'il avait apprise d'un oiseau qui parlait la veille. L'oiseau lui avait promis de le guider vers le fromage s'il chantait correctement la chanson.\
    En chevauchant, l'aventurier remarqua un groupe de chats couchés sur le bord du chemin. Ils l'observaient attentivement, leurs yeux brillant d'une lueur inquiétante. L'aventurier les ignora et poursuivit son voyage.\
    En tournant un virage sur le chemin, il vit une lueur au loin. Il pédala plus vite, son cœur battant d'excitation. Était-ce le morceau perdu de fromage mûr qu'il cherchait ?\
    En s'approchant de la lumière, il vit qu'elle venait d'une petite maison nichée dans une forêt d'arbres. Il descendit de son vélo et frappa à la porte. Il frappa trois fois et une vieille femme ridée lui ouvrit.\
    \"Puis-je vous aider ?\" demanda-t-elle, ses yeux brillant de malice.\
    \"Je cherche le morceau perdu de fromage mûr\", dit l'aventurier.\
    La vieille femme rit. \"Oh, cette vieille chose. Je l'ai trouvée il y a des années. Mais je te donnerai un sac magique de haricots en échange d'une chanson.\"\
    L'aventurier réfléchit un moment, puis commença à chanter la chanson qu'il avait apprise de l'oiseau qui parlait. La vieille femme sourit et lui remit le sac de haricots.\
    Il la remercia et enfourcha à nouveau son vélo, chevauchant sur le chemin pavé et retournant dans la terre de Paris. Pendant qu'il chevauchait, il ouvrit le sac de haricots et observa avec émerveillement comment ils ont poussé en une gigantesque plante de haricots magiques qui atteignait les nuages.\
    Et ainsi, l'aventurier a vécu heureux pour toujours, avec son fidèle vélo et un sac de haricots magiques. Le morceau perdu de fromage mûr a été oublié, mais le souvenir de l'aventure est resté avec lui pour toujours."


language = 'fr'

tld = 'fr'

myobj = gTTS(text=mytext, lang=language, tld=tld, slow=False)

myobj.save('french.mp3')

# os.system('afplay welcome.mp3')
