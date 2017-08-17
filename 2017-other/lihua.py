import itertools
import hashlib
dic = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890_-=+)(*&^%$#@!~`\|][{};:/.,<>?"
for i in range(1, 10):
    for passw in itertools.product(dic, repeat=i):
        m = hashlib.md5(''.join(passw)+'LiHua')
        if '1a4fb3fb5ee12307' in m.hexdigest():
            print "".join(passw)
            return 0