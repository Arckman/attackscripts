import string
import collections
import itertools

'''
refer:
1.https://zh.wikipedia.org/wiki/%E7%BB%B4%E5%90%89%E5%B0%BC%E4%BA%9A%E5%AF%86%E7%A0%81#1
2.https://www.youtube.com/watch?v=jSUfz67w-ZA&index=11&list=PL1H1sBF1VAKVmrjF1uWh5wK9a2IzmUjPc&app=desktop
'''
message='ATTACKATDAWN'
key='lemon'

def encrypt(message,key,multiplier=-1):
	compressed_message=message.lower()

	for punctuation in str(string.punctuation+' '):
		compressed_message=compressed_message.replace(punctuation,'')

	cycler=itertools.cycle(key.lower())
	long_key=''.join([cycler.next() for _ in range(len(compressed_message))])

	coded=[]

	for number in range(len(long_key)):
		cipher_letter=compressed_message[number]
		key_letter=long_key[number]
		cipher_index=string.ascii_lowercase.index(cipher_letter)
		key_index=string.ascii_lowercase.index(key_letter)

		lowercase=collections.deque(string.ascii_lowercase)
		lowercase.rotate(multiplier*key_index)
		new_alphabet=''.join(list(lowercase))
		new_character=new_alphabet[cipher_index]
		coded.append(new_character)

	return ''.join(coded)

def decrypt(message,key):
	return encrypt(message,key,1)

# print decrypt(encrypt(message,key),key)

'''
key =  Kkkkk kkkkKkkkkkkkkKkkkkkkkkKkk
flag = uucbx{simbjyaqyvzbzfdatshktkbde}
sha256 = 8304c5fa4186bbce7ac030d068fdd485040e65bf824ee70b0bdbac03862bec93
'''
encrypted='uucbxsimbjyaqyvzbzfdatshktkbde'

start_of_key=''
for p in itertools.permutations(string.ascii_lowercase,5):
	key=''.join(p)
	decrypted=decrypt(encrypted[:5],key)
	if decrypted=='tjctf':
		print key
		start_of_key=key
		break

import hashlib 

for p in itertools.permutations(string.ascii_lowercase,4):
	key=start_of_key+''.join(p)
	decrypted=decrypt(encrypted,key)
	flag=decrypted[:5]+'{'+decrypted[5:]+'}'

	s=hashlib.sha256()
	s.update(flag)
	that_hash=s.hexdigest()
	if that_hash=='8304c5fa4186bbce7ac030d068fdd485040e65bf824ee70b0bdbac03862bec93':
		print flag
		break
