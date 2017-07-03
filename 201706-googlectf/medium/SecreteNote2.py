import sqlite3
conn=sqlite3.connect('note.db')
c=conn.cursor()
r=''
c.execute('select * from Diff where DiffSet >=36;')
for s in c:
    _id,_insert,_position,_str,_set=s
    print('-------------id:%d------------'%(_id))
    l=len(_str)
    if _insert==1:
        tmp=r[:_position]+_str+r[_position:]
        r=tmp
    else:
        #assert(r[_position:_position+l]==_str)
        tmp=r[:_position]+r[_position+l:]
        r=tmp
    print(r)
