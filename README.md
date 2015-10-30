# numSplit

Console application taking 1 integer argument.  Creates an array of [input integer] values from 1 to [input integer].
Application will then split the array of values in half by every other number, throwing away one half (SPLIT) and continuing to split the other (R) until there is nothing left.

EX: numSplit.py 10

Input range: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

SPLIT: [1, 3, 5, 7, 9]
R: [2, 4, 6, 8, 10]

SPLIT: [2, 6, 10]
R: [4, 8]

SPLIT: [4]
R: [8]

SPLIT: [8]
R: []
