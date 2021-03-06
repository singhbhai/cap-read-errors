from notquitesoundex import notquitesoundex
from random import choice
#import nltk
#from nltk.corpus import cmudict
import re
from random import randint
from random import shuffle
import math

# gen phonetic error
zero = ['a', 'e', 'h', 'i', 'o', 'u', 'w', 'y' ]
one = ['b', 'f', 'p', 'v']
two = ['c', 'g', 'j', 'k', 'q', 's', 'x', 'z']
three = ['d', 't']
four = ['l']
five = ['m', 'n']
six = ['r']
#d = cmudict.dict()


def getletter(c):
	if c == '0':
		return choice(zero)
	elif c=='1':
		return choice(one)
	elif c=='2':
		return choice(two)
	elif c=='3':
		return choice(three)
	elif c=='4':
		return choice(four)
	elif c=='5':
		return choice(five)
	elif c=='6':
		return choice(six)


#given a word, generate a phonetically similar error
def genphonerr(wurd):
	if wurd.isdigit(): return wurd
	wurdcode = notquitesoundex(wurd) # the soundex alg's phonetic id looks like this: s0000
	err = wurdcode[0] # 
	#print 'wurdcode is ', wurdcode 
	wurdcode = wurdcode[1:] # only the numbers 
	#print 'wurdcode NOW is ', wurdcode 

	for w in wurdcode:
		err += getletter(w)
	return '['+err+']'

def genemptyword(word):
	return '[]'

"""def shuffle_word(word):
	word = list(word)
    	shuffle(word)
	return ''.join(word)
"""
def gentypo(word): 
	word = list(word)
	typolimit = int(math.ceil(0.2 * len(word)))#num of typos in a single word - let's make it 20% rounded up(ref WSL's email)

	for i in range(0,typolimit):
		word[randint(0, len(word)-1)] = choice('abcdefghijklmnopqrstuvwxyz ')#substs rndm lttr in word with another lttr at rndm
	return "["+''.join(word)+"]" #converts the list ver. of word back into a string
		
	

def gensomerr(word):
	#matchObj = re.match( r'[a-zA-Z0-9]+[^aeiou]+[^aeiou]+[a-zA-Z0-9]+', word)
	#if matchObj:
	choyce = choice(['empty', 'phonerr', 'typo'])
	
	if choyce=='empty':
		return genemptyword(word)
	elif choyce=='phonerr':
		return genphonerr(word)
	elif choyce=='typo':
		return gentypo(word)
	else:
		print 'this is mysterious error in genemptyword()'


"""def nsyl(word): #ignore this for now, I'm not using this. 
	return [(list(y for y in x if y[-1].isdigit())) for x in d[word.lower()]]
"""
#print 'generr is', genphonerr('thinking')
#print 'breakup is ', nsyl('cowf')




