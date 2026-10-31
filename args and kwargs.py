def fun(*args,**kwargs):
    print('Non keyword Arguments(args): ')
    for arg in args:
        print(args)
        
    print('Keyword Arguments (kwargs):')
    for key, value in kwargs.items():
        print(f"{key}=={value}")
        
fun('lav', 'dahake', first='lav', mid='kumar', last='dahake')