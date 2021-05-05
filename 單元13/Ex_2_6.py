from playrobot import STT,TTS
import jieba
import wikipedia
import re
wikipedia.set_lang("zh-tw")
target = input('wait command...')
while target != 'q':
    sound = STT.stt()
    head = ''
    words = jieba.lcut(sound)
    for word in words:
        if(word != u'是' and word != u'在'):
            head += word
        else:
            break
    message = wikipedia.summary(head,sentences=1)
    message2 = re.sub(u'[a-zA-Z(),（）「」]','',message)
    TTS.wordToSound(message2)
    target = input('wait command...')



