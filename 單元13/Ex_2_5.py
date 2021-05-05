import wikipedia
wikipedia.set_lang("zh-tw")
target = input()
while target != 'q':
    print(wikipedia.summary(target,sentences=1))
    target = input()
