def print_args(*args):
#   for arg in args:
#   print(f'arg = {arg}')

    print(args)
    print(type(args))

print_args('aaaa')
print_args('a','b','c','d')

#--------exemplo 2 --------#

def print_keyword_args(**kwargs):

    print('\n')
    print(kwargs)
    print(type(kwargs))

    for key, value in kwargs.items():
        print(f'{key} = {value}')

    third = kwargs.get('third', None)
    if third != None:
        print('third arg =', third)

print_keyword_args(first='a')
print_keyword_args(first='d', second='e', third='f')

