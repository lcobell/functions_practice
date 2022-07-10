
# arb_args -Takes in any number of arguments and prints them one at a time
from re import A, L


def arb_args(*args):
    for a in args:
        print(a)


# Takes in two integers.  Two nested functions should perform separate and distinct math ops.
# The result of both nested functions should then be added and printed together.


def inner_func(x, y):
    def inner_1():
        return x+y

    def inner_2():
        return x-y
    print(inner_1()+inner_2())

# Takes in two strings: student name and lunch choice. function prints both strings, if no pref prints "mystery meat"


def lunch_lady(name, lunch="mystery meat"):
    print(name, lunch)

# accepts two integers and returns both the sum and product


def sum_n_product(x, y):
    return x+y, x*y

# Should be arb_args but assigned an alias. Remember, variables can hold functions in python just like JS.
# You can make function call within another function.


alias_arb_args = arb_args

# Accepts any number of integers and prints their average


def arb_mean(*args):
    total = 0
    for a in args:
        total += a
    print(a/len(args))

# Acce[ts any number of strings and retunrs the longst]


def arb_longest_string(*args):
    long = 0
    longest = ""
    for a in args:
        if len(a) > long:
            long = len(a)
            longest = a
    return longest
