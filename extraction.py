# Write a Python program that reads a text file named numbers.txt that contains 20 integers. 
# The program will create two other text file; 
# the first text file will be named even.txt that will contains all even numbers extracted from the numbers.txt. 
# The second text file will be named odd.txt that will contains all odd numbers extracted from the numbers.txt.

# create method
def extract():
    # open numbers.txt(read), even.txt(append), odd.txt(append)
    with open("numbers.txt") as ref_file, open("even.txt", "a") as even_file, open("odd.txt", "a") as odd_file:
        # Designing the file
        import pyfiglet
        # read the numbers per line
        for line in ref_file:
            # convert to integer
            input_num = int(line)
            # if even,
            if input_num % 2 == 0:
            # append in even.txt
                even = str(input_num) + "\n"
                even_file.write(pyfiglet.figlet_format(even)) 
            # else, append in odd.txt
            else:
                odd = str(input_num) + "\n"
                odd_file.write(pyfiglet.figlet_format(odd))
# start
extract()