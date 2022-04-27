"""Given: A string s of length at most 10000 letters.

   Return: The number of occurrences of each word in s, where words are separated by spaces. 
           Words are case-sensitive, and the lines in the output can be in any order."""

 # Creating an empty dictionary and opening the file in read only mode and storing it in object 'f'.Then using read and 
 # split method to read and split(using whitespace as delimiter) the file into a list of words and stored in variable 'lines'.
my_dict = {}
with open("rosalind_ini6.txt", "r") as f:
    lines = f.read().rstrip('\n').split(" ")
    for word in lines:                      # Using for loop and if condition to add the words from the list 'lines' into
        if word not in my_dict:             # the empty dictionary 'my_dict'.
                my_dict[word] = 1
        else:
                my_dict[word] += 1           
for key in my_dict:                         # Using for loop with iteration variable key to loop through each key
    print(key, my_dict[key])                # and print key and value using key and my_dict[key] (for extracting value).