import re
from urllib import unquote
pattern='Set-Cookie: (\d*)=(.*?);'
_s=[]
for line in open(r'D:\security\WP\HackCon\2017\web\aa\magic.response').readlines():
    if line.startswith('Set-Cookie:'):
        i,c=re.search(pattern,line).groups()
        _s.append(c)
_s=''.join(_s)
print unquote(_s)


