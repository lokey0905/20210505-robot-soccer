import jieba
target = ''
while(target != 'quit'):
    target = input()
    words = jieba.lcut(target)
    print(words)