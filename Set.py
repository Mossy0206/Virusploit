# Sets get rid of duplicate values or strings.
# Very efficient at testing if a value is part of a set - Membership Test.
# Efficient at comparing with other set's - What values the share of don't share with other sets.

letters = {'A', 'b', 'c', 'X', 'M', 'f', 'K', 'A'}
compareLetters = {'A', 'b', 'c', 'X', 'M', 'f', 'K', 'Z'}
print('b' in letters)
print(letters.intersection(compareLetters))
print(compareLetters.difference(letters))