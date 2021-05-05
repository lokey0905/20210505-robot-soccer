def decorate(func):
    def inner(name):
        name = func(name)
        name = 'How are you?\n' + name
        return name
    return inner

@decorate
def print_hello(name):
    name = 'hello! '+name
    return name


print(print_hello('playrobot'))

