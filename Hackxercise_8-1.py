# Hackxercise_8-1

# Implement a function that given a URL, parses it and returns a tuple with its protocol, domain and path. For example, for "http://www.google.com/search", it whould return ('http', 'www.google.com', '/search').

# Check out urllib.parse.

from urllib.parse import urlparse

def parse_url(url):
    parsed = urlparse(url)
    return (parsed[0], parsed[1], parsed[2])
    
# test
print(parse_url("http://www.google.com/search"))