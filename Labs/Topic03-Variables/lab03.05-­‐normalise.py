# Program that reads in a string
# strips any leading or trailing spaces,
# converts into lower case,
# also outputs the length of the original and normalised string

rawstring = input("Please enter a string: ")
normalisedstring = rawstring.strip().lower()

lengthOfRawstring = len(rawstring)
lengthOfNormalisedstring = len(normalisedstring)

print("That string normalised is: {}". format(normalisedstring))
print("We reduced the input string from {} to {} characters".format(lengthOfRawstring, lengthOfNormalisedstring))