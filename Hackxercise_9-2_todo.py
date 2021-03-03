# Hackxercise_9-2

# Implement the function sign so that given a line (in bytes), returns a unique signature of that line that is 20 characters long;
# Implement the scan function that, given a list of paths and a signature, reads them line by line, and returns a list of all the paths that have a line that matches the static signature.
# Any line in a file might end with a ‘\n’. Remember to remove it.

# HINT
# Don’t leave open files.

# HINT
# SHA1 is a good way to get a digest of a string (Remember hashlib?).

# Your solution was successfully submitted.
# You passed 67% of all tests.

import hashlib

def sign(line):
    s = hashlib.sha1()
    s.update(line)
    h = s.hexdigest()
    return h[:20]

# TODO: correct the scan function
def scan(paths, signature):
    l = []
    for path in paths:
        f = open(path, "r")
        for x in f:
            if sign(x) == signature:
                l.append(x.rstrip("\n"))
        f.close()
    return l