# encoding: utf-8
import math


def is_prime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3, int(math.sqrt(number) + 1), 2):
            if number % current == 0:
                return False
        return True
    return False


def get_primes(start):
    while True:
        if is_prime(start):
            # other = yield foo  这样的语句的意思是返回foo，将foo的值赋值给other
            number = yield start
            if number is not None:
                print "send number is : ", number
        start += 1


# gen = get_primes(10)
# for i in gen:
#     if i < 200:
#         gen.send("110")
#         print i
#     else:
#         break

print "=========="


def print_successive_primes(interations, base=10):
    prime_generator = get_primes(base)
    prime_generator.send(None)
    for power in range(interations):
        print prime_generator.send(base ** power)


print_successive_primes(10)
