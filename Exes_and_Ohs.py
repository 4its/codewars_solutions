"""
Exes and Ohs.
Check to see if a string has the same amount of 'x's and 'o's.
The method must return a boolean and be case insensitive.
The string can contain any char.

Examples input/output:
XO("ooxx")      => true
XO("xooxx")     => false
XO("ooxXm")     => true
XO("zpzpzpp")   => true // when no 'x' and 'o' is present should return true
XO("zzoo")      => false
"""


def xo(s: str) -> str:
    return s.lower().count('x') == s.lower().count('o')


def xo2(s: str) -> str:
    s = s.lower()
    return s.count('x') == s.count('o')


print(xo("ooxx"))
print(xo("xooxx"))
print(xo("ooxXm"))

print(xo2("ooxx"))
print(xo2("xooxx"))
print(xo2("ooxXm"))
