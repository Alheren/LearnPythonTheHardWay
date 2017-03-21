"""
LPTHW Exercise 5 - More Variables and Printing

"""

MY_NAME = 'Zed A. Shaw'
MY_AGE = 35 # not a lie
MY_HEIGHT = 74 # inches
MY_WEIGHT = 180 # pounds
MY_EYES = 'Blue'
MY_TEETH = 'White'
MY_HAIR = 'Brown'

print "Let's talk about %s." % MY_NAME
print "He's %d inches tall." % MY_HEIGHT
print "He's %d pounds heavy" % MY_WEIGHT
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (MY_EYES, MY_HAIR)
print "His teeth are usually %s depending on the coffee." % MY_TEETH

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d, I get %d." % (
    MY_AGE, MY_HEIGHT, MY_WEIGHT, MY_AGE + MY_HEIGHT + MY_WEIGHT
)