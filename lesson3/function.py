def hello():
    print('hello')

def hello2(name, age):
    year = 2020 - age
    print('hello', name, 'your year of birth', year)
    print('hello '+name, 'your year of birth', year)

hello()
hello2('danya', 13)