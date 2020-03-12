# Olga Rozhdestvina
# a program that reads in a text file and outputs the number of e's it contains.

with open('ulysses.txt', 'r') as u:
    letter = (e.count('e') for e in u) # counts the letter 'e' in the text
    print(sum(letter)) # sums up the counts 
    
# An error "'int' object is not iterable" appeared 
# when "for e in u" is placed before defining 'letter'
# the simpliest solution found here https://stackoverflow.com/questions/41504428/find-the-number-of-characters-in-a-file-using-python