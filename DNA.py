"""Given: A DNA string s of length at most 1000 nt.

   Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' 
           occur in s."""
    
count_A = 0
count_T = 0
count_G = 0
count_C = 0
with open("rosalind_dna.txt" , 'r') as f:
    nt_str = f.read().rstrip()
    for nb in nt_str:
        if nb == 'A':
            count_A = count_A + 1
        elif nb == 'C':
            count_C = count_C + 1
        elif nb == 'G':
            count_G = count_G + 1
        else:
            nb == 'T'
            count_T = count_T + 1
print(count_A, count_C, count_G, count_T)
