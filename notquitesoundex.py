def notquitesoundex(name):
    """ ack: amended from Gregory Jorgensen's soundex module (see comment just below this)
    """	
    """ soundex module conforming to Knuth's algorithm
        implementation 2000-12-24 by Gregory Jorgensen
        public domain
    """

    # digits holds the soundex values for the alphabet
    digits = '01230120022455012623010202'
    sndx = ''
    fc = ''

    # translate alpha chars in name to soundex digits
    for c in name:
        if c.isalpha(): #is alphabet
            if not fc: fc = c   # remember first letter
            d = digits[ord(c)-ord('a')] #alphabet offset
            # duplicate consecutive soundex digits are skipped
            #if not sndx or (d != sndx[-1]):
            sndx += d

    # replace first digit with first alpha character
    sndx = fc + sndx[1:]

    # remove all 0s from the soundex code
    #sndx = sndx.replace('0','')

    # return soundex code padded to 

 #characters
    #return (sndx + (len * '0'))[:len]
    return sndx	
