def fun1():
    s=' hello from function 1'
    def fun2():
        print('hello from function 2')
        print(s)

    fun2()
fun1()        