"""
Think of you brain as a ML model. If it only sees great code,
it will not know what bad code is! So here is a _deliberately_ bad code
to add to the negative class.

And as Master Yoda said, there should always be a balance in the force. 
"""
from itertools import groupby

s = '1113222113'
ns = ''
for l in range(0, 50):
    ns = ''
    grouped = [list(g) for k, g in groupby(s)]
    for i in grouped:
        ns = ns+str(len(i))+i[0]
    s=ns
    if l ==39:
        print('Part 1 = ', len(ns))

print('Part 2 = ', len(ns))
