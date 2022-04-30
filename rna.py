"""Given a DNA string t corresponding to a coding strand, its transcribed RNA string u is formed by replacing all 
   occurrences of 'T' in t with 'U' in u.

   Given: A DNA string t having length at most 1000 nt.

   Return: The transcribed RNA string of t."""

with open('rosalind_rna.txt' , 'r') as f:   # Open the file in read only mode and save as object 'f'
    f = f.read().replace('T' , 'U')         # Read the file using 'read' method and replace 'T' with 'U' using replace method      
    print(f)


# Alternative solution : for those who doesn't know about replace method

# with open('rosalind_rna.txt') as f:           # Open the file in read only mode and save as object 'f'
#     print ("U".join(f.read().split("T")))     # Read the file and split at positions where 'T' is present and use 'join' method to
                                                # add 'U' in place of 'T' and print.