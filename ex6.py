"""
LPTHW - Exercise 6 - Strings and Text

"""
# This constant sets up the joke, this is string insertion point 1.
X = "There are %d types of people." % 10

# This Constant is self explainatory.
BINARY = "binary"

# Please pardon the state this contraction is in.
DO_NOT = "don't"

# This constant is the punchline and contains 2 additional string insertion points (total 3)
Y = "Those who know %s and those who %s." % (BINARY, DO_NOT)

# These 'print' statements tell the joke and punchline.
print X
print Y

# Repeating previous lines, while utilizing additional string insertions (total 5)
print "I said: %r." % X
print "I also said: '%s'." % Y

# More contant values to be played with
HILARIOUS = False

# This contant has a string insertion added to it, I have to remember I can do that. (total 6)
JOKE_EVALUATION = "Isn't that joke so funny?! %r"

# This uses the constant with the string insertion stored within it,
# and then uses another constant to provide the string.
print JOKE_EVALUATION % HILARIOUS

# Seperate constants...
W = "This is the left side of..."
E = "a string with a right side."

# brought back together with a print statement.
print W + E
