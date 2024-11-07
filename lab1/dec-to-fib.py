#!/usr/bin/python3
def fib(n):
    return 1 if n <= 1 else fib(n - 1) + fib(n - 2)

def decToFib(num):
    res = 0

    cache = {}
    while num > 0:
        fib_num = 0
        n = 1
        while fib_num <= num:
            if n in cache.keys():
                fib_num = cache[n]
            else:
                cache[n] = fib(n)
                fib_num = cache[n]
            n += 1
        n -= 1 # после выхода из цикла n - для числа fib_num >= num
        res += 1 * (10 ** (n - 1)) # (n - 1) - 1, т. к. 1-й разряд - 10 ** 0
        num -= 1 if n <= 1 else cache[n - 1]
        
    return res // 10

if __name__ == "__main__":
    num = int(input())
    print(decToFib(num))
