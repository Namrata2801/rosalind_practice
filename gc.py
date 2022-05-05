"""Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

   Return: The ID of the string having the highest GC-content, followed by the GC-content of that string.
           Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated."""
# defining a function 'readfile' to read a file and return a list of lines.
def readfile(filename):
    with open(filename, 'r') as f:
        return [l.strip() for l in f.readlines()]   # list comprehension used in function 'readfile'. In this comprehension for 
                                                    # loop is used to iterate through each line and strip any whitespaces at 
                                                    # the end returning a list of lines.

# defining a function 'gc_content' to calculate the gc% of fasta files   
def gc_content(seq):
    return round (((seq.count('C') + seq.count('G')) / len(seq) * 100) , 5) # using 'count' method and round function to count GC
                                                                            # content and return the gc% upto five decimal points.

# Calling 'readfile' function and storing the list of lines in variable 'fastafile'. 
fastafile = readfile("rosalind_gc.txt")

# Initializing an empty dictionary to use in the following for loop to create key, value pair of fastaID and nt sequence.
fastadict = {}

# Creating an empty string for fastaIDs to be used in following loop.
fastalabel = ""

for line in fastafile:                   # Using for loop to iterate through each element of the list 'fastafile '.
    if '>' in line:                      # Using if condition to find elements containing '>' sign and if true
        fastalabel =line                 # add that element as key in dictionary 'fastadict'.
        fastadict[fastalabel] = ""       
    else:
        fastadict[fastalabel] += line    # if element doesn't contain '>' sign then add that element as value of the previously added key.

# Creating another dict 'resultdict'. Using dictionary comprehension and 'gc_content' function to store the key and gc_content of the values (nt seq) 
resultdict = {key : gc_content(value) for (key,value)in fastadict.items()}

# using 'max' function and 'get' method to find the key with maxium gc_content.
max_gckey = max(resultdict, key = resultdict.get)

# print the key skipping the '>' sign in the fastaID
print(max_gckey[1:])

# print the value(gc_content) of the key with max value.
print(resultdict[max_gckey])
