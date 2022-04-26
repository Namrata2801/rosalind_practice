"""Given: A file containing at most 1000 lines.

Return: A file containing all the even-numbered lines from the original file. Assume 1-based numbering of lines."""

# Creating an empty list "Filtered_lines" and using "With open" syntax and 'r' mode to open and read the file
# and store it in 'f' object. This syntax closes the file automatically after the job is done eliminating the need to close the file.
filtered_lines = []
with open("rosalind_ini5.txt", "r") as f:
    lines = f.readlines()
    no_of_lines = len(lines)

    ## First alternative method using for loop, range(len(lines)) and if condition to iterate and extract only even numbered lines.
    #  Then using append method to add even numbered lines in the "filtered_line" list.

    # for i in range(no_of_lines):
    #     if i%2 == 1:
    #         print(lines[i])
    #         filtered_lines.append(lines[i])


    ## Second alternative method using for loop, range(start,end,step size) to iterate only even numbered lines and 
    #  append method to add even numbered lines in the "filtered_line" list.

    # for i in range(1 , no_of_lines , 2):
    #     print(lines[i])
    #     filtered_lines.append(lines[i])
    ##

    # Using list comprehension below to extract even numbered lines from the file in list "Filtered_lines".
    filtered_lines = [lines[i] for i in range(1, no_of_lines, 2)]

# Storing the contents of filtered_lines list into an output file "output_ini5.txt" using 'w' mode and writelines method.
with open("output_ini5.txt", 'w') as f:
    f.writelines(filtered_lines)

    