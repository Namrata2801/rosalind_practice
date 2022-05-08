"""Given: Two DNA strings s and t (each of length at most 1 kbp).

   Return: All locations of t as a substring of s."""


 # Open the file in read only format and use 'readlines' method to produce a list containing parent DNA string and substring.
with open("rosalind_subs.txt" , 'r') as f:
     f = f.readlines()
ps = f[0].rstrip()                    # save the parent DNA seq in variable 'ps' after removing new line character present at the end .
ss = f[1].rstrip()                    # save the subsequence in variable 'ss' after removing new line character  .
ans = [str(i + 1) for i in range(len(ps)) if ps.startswith(ss, i)]    # Use list comprehension containing for loop, if condition and startswith method
print(' '.join(ans))                                                  # to search for the DNA substring in parent DNA string. The iterating variable scans through each
                                                                      # DNA nt in parent seq(ps) looking for seq starting with the substring(ss). The resulting index is an
                                                                      # integer starting from 0. The position is increased by 1 after adding 1 to the iterating variable.
                                                                      # str method is used to convert the value into string from integer.
                                                                      # To remove comma and square brackets the result is printed using whitespace as delimiter and join method to give index position in form of string.