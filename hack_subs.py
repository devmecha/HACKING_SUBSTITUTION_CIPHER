import copy, pprint
import time, os, sys
import math, re
import wPs, subs_cipher

status =''
S = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
l = len(S)

#Functions

def emptyM():
	return {'A': [], 'B': [], 'C': [], 'D': [], 'E': [], 'F': [], 'G': [],
           'H': [], 'I': [], 'J': [], 'K': [], 'L': [], 'M': [], 'N': [],
           'O': [], 'P': [], 'Q': [], 'R': [], 'S': [], 'T': [], 'U': [],
           'V': [], 'W': [], 'X': [], 'Y': [], 'Z': []}

def addChar(lm, word, pt):
	li = len(word)
	for d in range(li) :
		if pt[d] not in lm[word[d]]:
			lm[word[d]].append(pt[d])

def colXY(X, Y):
	R = emptyM()
	for c in S:
		if X[c] == []:
			R[c] = copy.deepcopy(Y[c])
		elif Y[c] == []:
			R[c] = copy.deepcopy(X[c])
		else:
			for cc in X[c]:
				if cc in Y[c]:
					R[c].append(cc)
	return R

def del_If_Found(lm):
	u = len(lm) 
	fl = True
	while fl:
		fl = False
		found = []
		for c in S:
			if len(lm[c]) == 1:
				found.append(lm[c][0])
		for c in S:
			for f in found:
				if f in lm[c] and len(lm[c]) != 1:
					lm[c].remove(f)
					if len(lm[c]) == 1:
						fl = True
	return lm

def hack_subs(msg, S, l):
	R = emptyM()
	ardi = re.compile('[^A-Z\s]')
	mMsg = ardi.sub('',msg.upper()).split() # Divide and Conquer
	for wd in mMsg:
		ptmp = emptyM()
		wdP = toPattern(wd)
		if wdP not in wPs.Ps:
			continue
		for pt in wPs.Ps[wdP]:
			addChar(ptmp, wd, pt)
		R = colXY(R, ptmp)
	return del_If_Found(R)

def dec(msg, lm, S):
	k = ['*'] * l
	for c in S:
		if len(lm[c]) == 1:
			k_index = S.index(lm[c][0])
			k[k_index] = c
		else:
			msg = msg.replace(c.lower(),'?')
			msg = msg.replace(c.upper(),'?')
	k =''.join(k)
	return subs_cipher.subs_dec(msg, k, S)

def toPattern(wd):
    # Returns a string of the pattern form of the given word.
    # e.g. '0.1.2.3.4.1.2.3.5.6' for 'DUSTBUSTER'
    wd = wd.upper()
    n = 0
    Num = {}
    wdP = []

    for c in wd:
        if c not in Num:
            Num[c] = str(n)
            n += 1
        wdP.append(Num[c])
    return '.'.join(wdP)

def callPs():
	Ps = {}
	df = open('dictionary.txt')
	wds = df.read().split('\n')
	df.close()
	for wd in wds:
		p = toPattern(wd)
		if p not in Ps:
			Ps[p] = [wd]
		else:
			Ps[p].append(wd)
	df = open('wPs.py', 'w')
	df.write('Ps = ')
	df.write(pprint.pformat(Ps))
	df.close()


#Main

def Main():
	print("****** HACKING || THE SUBSTITUTIN CIPHER *******")
	print('+++++++++++++++++++++++++++++++++++++++++++++++++')
	msg = input('Please Enter your Message : ')
	print('\n')
	# Infos
	print('-------------All in All------------------')
	print('List of symbols : %s ' %S )
	print('\n')
	print('Your message is : %s ' %msg )
	print('-----------------------------------------')
	# Continue ?
	print('You want to continue ? (Y)es or (N)o ?')
	response = input('> ')
	if not response.lower().startswith('y'):
		sys.exit()
	#
	print('Processing now ...' )
	timer = time.time()
	lm = hack_subs(msg, S, l)
	res = dec(msg,lm, S)
	print(res)
	t = round(time.time() - timer, 2)
	print('-------------------------------------------')
	print('List of symbols : %s ' %S )
	print('\n')
	print('Your message is : %s ' %msg )
	print('\n')
	print('Your Potential Decrypted message is : %s ' %res )
	print('\n')
	print('Process time : %s ' %t )
	print('-------------------------------------------')
	
if __name__ == '__main__':
 	Main()