import re

def camel(token):
    a = re.split(r'-|_', token)
    print(a)
    string = ""
    walker = 0
    walker2 = 0

    for i in a:
        walker = 1
        for n in i:
            if walker == 1 and walker2 == 0:
                string += n
                walker2 = 1
                walker = 0
            elif walker == 1:
                string += n.upper()
                walker = 0
            else:
                string += n

    return string

token = "the-stealth_warrior"
a = camel(token)
print(a)
