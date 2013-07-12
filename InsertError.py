from random import shuffle
import math
from decimal import *
import os
import shutil
from random import choice
from Genphoneticerror import gensomerr
# future stuff: Chuck all print statements in a logfile; modify for multiple input files; 
# (optional) create a better garble_word; This is uniform dist of errors - create nonuniform dis of errors
f = open('input4.txt', 'r') #input file: rename to whatever your input filename is, if you want. 
sCon = f.read() #string of the contents - I actually don't need this at all. Didn't work very well.
lCon = sCon.split() # list of words in file
lenn = len(lCon) # num of words in file. 
error_rate = raw_input("Enter the error rate (eg., 0.1, 0.3, 0.5): ")#from our eg, 0.2 (between 0.0 and 1.0)
error_rate = Decimal(error_rate)
print 'error rate is ', error_rate
numErrors = int(error_rate * Decimal(len(lCon))) #from our eg, 0.2 of 95 words yields 19 words
print 'numErrors is ', numErrors
maxspacing = math.floor((lenn-1)/(numErrors -1)) -1 #max spacing is flr(length -1 / numErrors -1) -1
print 'maxspacing is ', maxspacing# this is the least clustered errors can be. ie, has least continuity at maxspacing.


# this inserts the error given the # of errors (say 19) and spacing (say 2 spaces apart) 
# we'll have a loop in runmain() that prints out a file with diff vals of spacing (eg: 0-4 for 0.2 err_rate) to diff output files
def inserterr(l, spacing, numerr):
	i = 0
	changedone = 0
	while i < len(l):
		l[i] = gensomerr(l[i])# this rdmly generates a phonetic error or string of empty spaces. 
		changedone = changedone + 1 
		if changedone >= numErrors: #once we reach numErrors, we quit. That's all the errors we want in our text. 
			break
		i = i + spacing+1
	print 'changedone : ', changedone # this works! It totals up to 19! My maxspacing calc rocks.		
	return ' '.join(l)

#loop in runmain() prints out a file with diff vals of spacing (eg: 0-4 for 0.2 err_rate) to diff output files
def runMain():
	
	if os.path.exists('outpoot'): 
		shutil.rmtree('outpoot') #deletes (previous) nonempty folder (this cmd fails on readonly files though)
    	os.makedirs('outpoot')	# makes new empty folder

	# now we create a loop to make new o/p docs for diff values of spacing
	j=0
	while j <= maxspacing:
		copylCon = list(lCon) # create a fresh copy for every iteration, because lists are mutable and passbyref in python
		paath = os.getcwd()+'/outpoot/outputwith'+str(j)+'spaces.txt'#filename
		fw = open(paath, "w")
		fw.write(inserterr(copylCon, j, numErrors))
		fw.flush()
		fw.close()
		j = j+1
	

def shuffle_word(word):
	word = list(word)
    	shuffle(word)
    	return ''.join(word)

runMain() 
