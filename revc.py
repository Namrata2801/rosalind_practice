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




