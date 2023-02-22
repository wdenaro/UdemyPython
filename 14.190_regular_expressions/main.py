# Regular expressions

import re

# pattern = re.compile('this')
#
# str = 'search inside of this text please!'
#
# a = pattern.search(str)
#
# b = pattern.findall(str)
#
# c = pattern.fullmatch(str)
#
# d = pattern.match(str)
#
# print(a.span())
# print(a.start())
# print(a.end())
# print(a.group())
#
# print(b)
#
# print(c)
#
# print(d)


pattern = re.compile(r"([a-zA-Z]).([a])")
string = 'search this inside of this text pleas! Andrei'

a = pattern.search(string)

print(a.group())