# 19. Create a function which will take unlimited arguments both non keyword and
# keyword arguments. Add the values of all non keyword arguments and also the
# value of keyword arguments.


def myfunc(*args, **kwargs):
    args = 0
    kwargs = 0
    for i in args:
        args += i
    return args



print(myfunc(10,20))


