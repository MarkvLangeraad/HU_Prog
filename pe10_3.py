user = input('Enter your name:')
begin_station = input('Enter your beginstation:')
end_station = input('Enter your endstation:')
invoerstring = user+begin_station+end_station

def code(invoerstring):
    zaza = ([ord(c)for c in invoerstring])
    coco = [(3+c) for c in zaza]
    dede = ([chr(d) for d in coco])
    zuzu = ''.join(dede)
    keke = print(zuzu)
    return keke

code(invoerstring)


