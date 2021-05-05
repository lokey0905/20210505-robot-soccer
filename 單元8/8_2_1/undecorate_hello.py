def print_hello(name):
    name = 'hello! '+name
    return name

#print(print_hello('playrobot'))

def decorate(func):
    def inner(name):
        name = func(name)
        name = 'How are you?\n' + name
        return name
    return inner

print_hello = decorate(print_hello)

print(print_hello('playrobot'))

