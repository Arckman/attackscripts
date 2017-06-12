from PIL import Image
import requests
import sys

s=r'abcdefGHIJKL.png'
s=r'abcdefGHIJKLmnopgrSTUVWZ.png'
s='a'*24+'.png'
s='b'*24+'.png'
s='Z'*24+'.png'
s='_'*24+'.png'
tmp=r'temp.png'
def getcontent(s=tmp,text='error'):
    im=Image.open(s)
    #im.show()
    #print im.size,im.mode
    print text
    l=len(text)
    for i in range(0,l/3):
        r,g,b=im.getpixel((2+40*i,2))
        print '%s(%d),%s(%d),%s(%d):[%s(%d),%s(%d),%s(%d)]'%(bin(ord(text[i*3])),ord(text[i*3]),bin(ord(text[i*3+1])),ord(text[i*3+1]),bin(ord(text[i*3+2])),ord(text[i*3+2]),bin(r),r,bin(g),g,bin(b),b)
        #print '%s(%d),%s(%d),%s(%d)'%(bin(ord(text[i*3])),ord(text[i*3]),bin(ord(text[i*3+1])),ord(text[i*3+1]),bin(ord(text[i*3+2])),ord(text[i*3+2]))+":"+str(im.getpixel((2+40*i,2)))
        #print '%d,%d,%d'%(ord(text[i*3]),ord(text[i*3+1]),ord(text[i*3+2]))+":"+str(im.getpixel((2+40*i,2)))

def tencode(text):
    global tmp
    u=r'https://cryptoengine.stillhackinganyway.nl/encrypt?text='
    re=requests.get(u+text)
    f=open(tmp,'wb')
    f.write(re.content)
    f.close()

l=['!', '"', '$', '%', "'", '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8',
 '9', ':', ';', '<', '=', '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[','\\',']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'
, 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~']

argvs=sys.argv
if len(argvs)==1:
    #gei all char*24
    '''
    for c in l:
        tencode(c*24)
        getcontent(tmp,c*24)
    '''
    #get abcdefGHIJKLmnopgrSTUVWZ
    '''
    tencode('abcdefGHIJKLmnopgrSTUVWZ')
    getcontent(tmp,'abcdefGHIJKLmnopgrSTUVWZ')
    '''
    #get flag target
    #getcontent('flag.png',' '*36)

    #decode flag
    nums=[84, 92, 80, 80, 47, 56, 53, 49, 73, 1, 13, 2, 44, 99, 62, 54, 73, 87, 6, 3, 42, 50, 63, 103, 24, 83, 89, 1, 40, 50, 60, 53, 28, 84, 4, 0, 46, 41]
    l=len(nums)
    for i in range(l-1,-1,-1):
        if i-4>-1:
            nums[i]^=nums[i-4]
    re=''
    for i in range(4,l):
        re+=chr(nums[i])
    print 'flag'+re
elif len(argvs)==2:
    tencode(argvs[1])
    getcontent(tmp,argvs[1])
