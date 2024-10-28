#Write a script that creates a new output file called myfile.txt and writes the string "Hello file world!" in it.
file = open('myfile.txt', 'w')
file.write('Hello file world!')
#Then write another script that opens myfile.txt, and reads and prints its contents.
file = open('myfile.txt', 'r')
read = file.readlines()
print(read)
