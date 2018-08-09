import numpy as np
result='1001100001011110110100001100001010000011110101001100100011101111110100011111010101010000000110000011101101110000101111101010111011100101000011011010110010100001100010001010101001100001110110100110011101'
np.random.seed(12345)
other = np.random.randint(1,5,(len('ligma_sugma_sugondese_')*5))
lmao = [ord(x) for x in ''.join(['ligma_sugma_sugondese_'*5])]
i=0
import string
strs=string.printable
def walk(start,i,flag=np.array([])):
	if start==len(result):
		print 'At last:'+''.join(flag)
	else:
		for x in strs:
			arr=other[i]*ord(x)
			c=arr^lmao[i]
			c=bin(c)[2:].zfill(8)
			if result.startswith(c,start):
				print ''.join(flag)+x
				walk(start+len(c),i+1,np.append(flag,[x]))

walk(0,i)