import itertools
N=6266565720726907265997241358331585417095726146341989755538017122981360742813498401533594757088796536341941659691259323065631249
e1=773
e2=839
c1=3453520592723443935451151545245025864232388871721682326408915024349804062041976702364728660682912396903968193981131553111537349
c2=5672818026816293344070119332536629619457163570036305296869053532293105379690793386019065754465292867769521736414170803238309535

s1=s2=1
for s1,s2 in itertools.product(range(100),repeat=2):
    if e2*s2-e1*s1 == 1:
        break
print s2,s1

def fastExpMod(b, e, m):
    """
    key function for RSA decryption
    @param b:cipher
    @param e:e
    @param m:N
    e = e0*(2^0) + e1*(2^1) + e2*(2^2) + ... + en * (2^n)

    b^e = b^(e0*(2^0) + e1*(2^1) + e2*(2^2) + ... + en * (2^n))
        = b^(e0*(2^0)) * b^(e1*(2^1)) * b^(e2*(2^2)) * ... * b^(en*(2^n))

    b^e mod m = ((b^(e0*(2^0)) mod m) * (b^(e1*(2^1)) mod m) * (b^(e2*(2^2)) mod m) * ... * (b^(en*(2^n)) mod m) mod m
    """
    result = 1
    while e != 0:
        if (e&1) == 1:
            # ei = 1, then mul
            result = (result * b) % m
        e >>= 1
        # b, b^2, b^4, b^8, ... , b^(2^n)
        b = (b*b) % m
    return result

def fastMulMod(a,b,N):
    """
    same as fastExpMod
    """
    result = 0
    while b != 0:
        if (b&1) == 1:
            result = (result + a) % N
        b >>= 1
        # b, b^2, b^4, b^8, ... , b^(2^n)
        a= (a*a) % N
    return result

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
    return (g, x - (b // a) * y, y)

def modinv(a, m):
    '''
    模反函数求解
    '''
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist,is a and m prime to each?')
    else:
        return x % m


#RSA共模攻击求解，
#计算s1,s1使得s1*e1-s2*e2=1
#m=(c1^s1*c2^-s2)mod N ====> (c2^-s2)mod N==((c2^-1)mod N)^s2 mod N
c1=modinv(c1,N)
#print fastExpMod(c2,s2,N)
#print fastExpMod(c1,s1,N)
m=fastMulMod(fastExpMod(c2,s2,N),fastExpMod(c1,s1,N),N)
print m
