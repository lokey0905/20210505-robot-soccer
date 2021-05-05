from playrobot import TTS

def main():
    print('input a sentence to TTS!')
    text = input()
    TTS.wordToSound(text)

if __name__ == '__main__':
    main()

