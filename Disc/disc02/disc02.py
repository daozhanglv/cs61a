def keep_ints(cond, n):
    i = 1
    while i <= n:
        if cond(i):
            print(i)
        i += 1
        
def make_keeper(n):
    def condition(cond):
        i = 1
        while  i <= n:
            if cond(i):
                print(i)
            i += 1
    return condition

uncurry = lambda h: lambda x: lambda y: h(x,y)

def print_delayed(x):
    def print_now(y):
        print(x)
        return print_delayed(y)
    return print_now


def print_n(n):
    i = n
    def print_l(x):
        nonlocal i
        while i == 0:
            print("done")
            return print_l
        print(x)
        i -= 1
        return print_l
    return print_l
