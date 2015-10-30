############################################
## numSplit.py
##
## Console input.  Uses user input number x,
## builds an array of x length, and removes
## every other number until nothing is left.
##
## EX: numSplit.py [number]
#############################################
import sys

# Check number of arguments
if (len(sys.argv) < 2):
    print "The arguments must contain 1 integer."
    sys.exit(0)

# Second input value is an integer, parse as integer
nIn = int(sys.argv[1])
# Make array of 0s of size (nIn + 1)
nlist = [0] * (nIn + 1)
# Save length of list
length = len(nlist) - 1

# Build list starting with 1
# EX: [1, 2, 3, ... nIn]
x = 1
while (x < (nIn + 1)):
    nlist[x] = x
    x = x + 1

# Print the generated list
print "Input range: ", nlist[1:]

# Begin splitting list into halves
# slist is split list which is throw away on each iteration
# rlist is the remainder list which is saved and split on the next iteration 
rlen = length
slen = length
i = 1
d = 1
while((2*i - 1)*d <= length):
    slen = rlen
    rlen = rlen / 2
    slen = slen - rlen
    
    slist = [0] * (slen)
    rlist = [0] * (rlen)

    while((2*i - 1) * d <= length):
        slist[i - 1] = nlist[(2*i - 1)*d]
        if ((2*i*d) <= length):
            rlist[i - 1] = nlist[(2*i)*d]
        i = i + 1
    print ""
    print "SPLIT: ", slist
    print "R: ", rlist

    d = d*2
    i = 1
