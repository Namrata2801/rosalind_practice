"""In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.

   The reverse complement of a DNA string s is the string sc formed by reversing the symbols of s, then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").

   Given: A DNA string s of length at most 1000 bp.

   Return: The reverse complement sc of s."""

with open('rosalind_revc.txt' ,'r') as f: 
    f = f.read().rstrip()
    rc_dna = ''                      # Initializing an empty string 'rc_dna'
    for nts in f:                    # using for loop to iterate through each nucleotide.
        if nts == "A":               # using if/else condition to check the type of nucletide and replace with complementary nucleotide.
            rc_dna += "T"            # Appending the complementary nucleotide in the empty string.
        elif nts == "G":
            rc_dna += "C"
        elif nts == "T":
            rc_dna += "A"
        else:
            nts == "C"
            rc_dna += "G"
    rc_dna = rc_dna[::-1]           #  Reversing the sequence of characters in a string using slicing technique: string[start:stop:step-size]        
    print(rc_dna)                       


# # Alternative method 1: Using lower case letters as replacement nucleotides and 'upper' method to create the complementary DNA seq.
# #                       Then using slicing method to reverse the sequence of nucleotides.
# with open('rosalind_revc.txt' ,'r') as f: 
#     f = f.read()
#     f = f.replace('A', 't').replace('T', 'a').replace('C', 'g').replace('G', 'c').upper()[::-1]
#     print (f)



# Alternative method 2: Using 'translate' and 'maketrans' method of str class to create complementary sequnce
#                       Then using slicing method to reverse the sequence of nucleotides.
# with open('rosalind_revc.txt' ,'r') as f: 
#     f = f.read()
#     print(f[::-1].translate(str.maketrans('ACGT', 'TGCA')))


