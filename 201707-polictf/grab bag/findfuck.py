import sys
fuck=[]
for l in open('fuck.txt').readlines():
    fuck.append(l.strip())

for i,f in enumerate(fuck):
    indx=f.find(sys.argv[1])
    if indx!=-1 and indx<=int(sys.argv[2]):
        print '%d:Find str in fuck.txt,index is (%d)'%(i+1,indx)
