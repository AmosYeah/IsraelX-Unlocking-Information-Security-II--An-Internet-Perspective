# Hackxercise_9-3

# Write code that metamorphs the following expressions:

# x = x · 2
# s = 0
# for i in range(n):
#     s += i

def first(x):
    x = x + x
    return x

# s = 0
# for i in range(n):
#     s += i
# return s

def second(n):
    s = (1 + n - 1) * (n - 1) / 2
    return s