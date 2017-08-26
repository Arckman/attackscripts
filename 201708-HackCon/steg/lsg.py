from PIL import Image
import re
def getLSB(pixel):
    return str(bin(pixel))[-1]

header, trailer = 2*"11001100",2*"0101010100000000"
im=Image.open(r'D:\security\WP\HackCon\2017\Steg\Secret.png')
pixels,mode=list(im.getdata()),im.mode
s=''
for i in range(len(pixels)):
    s+=getLSB(pixels[i][i%len(mode)])
#print s
s=re.search('^'+header+'([01]*)'+trailer,s).group(1)
flag=[]
for i in range(0,len(s),8):
    flag.append(chr(int(s[i:i+8],2)))
print ''.join(flag)