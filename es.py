# Olga Rozhdestvina
# a program that reads in a text file and outputs the number of e's it contains.

with open('ulysses.txt', 'r') as u:
    print(sum(e.count('e') for e in u))
    
# I kept getting an error "unexpected EOF while parsing" when placed "for e in u" before print(),  found solution on https://stackoverflow.com/