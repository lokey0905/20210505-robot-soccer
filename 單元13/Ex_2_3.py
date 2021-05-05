from playrobot import TTS,STT
import io
def main():
    target = STT.stt()
    #target = input()
    
    #固定回應區
    with io.open('keysentence.txt', encoding = 'utf-8-sig') as f:
        keysentence = f.read()
        keysentence = keysentence.split(u'\n')
    
    with io.open('reply.txt', encoding = 'utf-8-sig') as f:
        reply = f.read()
        reply = reply.split(u'\n')
    
    temp_index = 0
    for tempKey in keysentence:
        tempKey = tempKey.split(u'\t')
        for temp in tempKey:
            if(target == temp):
                print(reply[temp_index])
                TTS.wordToSound(reply[temp_index])
        temp_index += 1

if __name__ == '__main__':
    if input() == 's':main()


