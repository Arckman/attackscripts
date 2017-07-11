import Levenshtein

def distance(str1):
    re={}
    for i,l in enumerate(open('fuck.txt').readlines()):
        re[Levenshtein.distance(str1,l)]=i+1
    re=sorted(re.iteritems(),key=lambda d:d[0])
    for d in re:
        print '%d,Distance is %d'%(d[1],d[0])
