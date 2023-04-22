# Write a Python program that reads a text file named numbers.txt that contains 20 integers. 
# The program will create two other text file; 
# the first text file will be named even.txt that will contains all even numbers extracted from the numbers.txt. 
# The second text file will be named odd.txt that will contains all odd numbers extracted from the numbers.txt.

# create method
def extract():
    # open numbers.txt(read), even.txt(append), odd.txt(append)
    with open("numbers.txt") as ref_file, open("even.txt", "a") as even_file, open("odd.txt", "a") as odd_file:
        # read the numbers per line
        for line in ref_file:
            # convert to integer
            input_num = int(line)
            # if even,
            if input_num % 2 == 0:
            # append in even.txt
                even_file.write(str(input_num) + "\n") 
            # else, append in odd.txt
            else:
                odd_file.write(str(input_num) + "\n")

# Designing the file

# start
extract()