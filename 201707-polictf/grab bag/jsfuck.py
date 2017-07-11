import re
fuck=[]
aph=[]

for l in open('aph.txt').readlines():
    aph.append(l.strip())
for l in open('fuck.txt').readlines():
    fuck.append(l.strip())

#print aph
#print len(aph)
#print fuck
#print len(fuck)


s=open('challenge2.js').readline().strip()
#print len(s)


def manual():
    stack=[]
    while(True):
        for i,f in enumerate(fuck):
            indx=s.find(f)
            if indx!=-1:
                print 'Find str(%s), index is %d'%(aph[i],indx)
        choice=raw_input('Please input your choice:')
        if choice in aph:
            f=fuck[aph.index(choice)]
            indx=s.find(f)
            s=s[:indx]+choice+s[len(f)+indx:]
            stack.append((choice,indx))
            print s
            print '==================================================================================='
        elif choice=='rr':
            c,pos=stack.pop()
            s=s[:pos]+fuck[aph.index(c)]+s[pos+1]
            print 'Backword...'
            print s
            print '==================================================================================='
        else:
            pass

def auto():
    global s
    while(True):
        best=('',100000)
        for i,f in enumerate(fuck):
            indx=s.find(f)
            if indx!=-1:
                print 'Find str(%s), index is %d'%(aph[i],indx)
                if indx<best[1]:
                    best=(aph[i],indx)
        if best[1]!=100000:
            print('Replacing str(%s)...'%(best[0]))
            f=fuck[aph.index(best[0])]
            indx=best[1]
            s=s[:indx]+best[0]+s[len(f)+indx:]
            #stack.append((choice,indx))
            print s
            print '==================================================================================='
        else:
            break

auto()
