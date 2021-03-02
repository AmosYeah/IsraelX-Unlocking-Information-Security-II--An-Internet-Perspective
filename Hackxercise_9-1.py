# Hackxercise_9-1

# Write a Python quine — that is, a program that prints its own source code. As a bonus, try coming up with a version different to the one in the text unit.

# The quine must not return the function statement – only its content. I.e., if your code is:

# def foo():
# 	return 123
# What should be returned is

# return 123
# And not:

# def foo():
# 	return 123

def quine():
    s='s=%r;print(s%%s)';print(s%s)
    return s
    
quine()