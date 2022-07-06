
# function hello
def hello():
    print("Hi there!")

# function pack that accepts 3 arguments and returns them as a list


def pack(a, b, c):
    return [a, b, c]
# function eat_lunch, accepts a list and prints a series of strings


def eat_lunch(my_lst):
    if len(my_lst) == 0:
        print("My lunchbox is empty")
    else:
        for i in range(len(my_lst)):
            if i == 0:
                print(f"First I eat {my_lst[0]}")
            else:
                print(f"Next I eat {my_lst[i]}")


hello()
print(pack("a", "b", "c"))
print(pack(1, 2, 3))
eat_lunch([])
eat_lunch(["sandwich"])
eat_lunch(["apple", "sandwich", "cookie"])
