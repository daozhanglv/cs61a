def mul(m,n):
    if n == 1:
        return m*n
    else:
        return m + mul(m,n-1)

def hailstone(n):
    print(n)
    if n == 1:
        return 1
    else:
        if n % 2 == 0:
            return hailstone(n // 2) + 1
        return hailstone(3 * n + 1) + 1
 
def merge(n1,n2):
    if n1 == 0:
        return n2
    elif n2 == 0:
        return n1
    elif n1 % 10 < n2 % 10:
        return n1 % 10 + merge(n1 // 10, n2)* 10
    else:
        return n2 % 10 + merge(n1, n2 // 10)* 10

def make_func_repeater(f, x):
    def repeat(n):
        if n == 0:
            return x
        else:
            return f(repeat(n-1))
    return repeat

def is_prime(n):
    def is_prime_helper(index):
        if index == n:
            return True
        elif n == 1 or n % index == 0:
            return False
        else:
            return is_prime_helper(index + 1)
    return is_prime_helper(2)
        
        
