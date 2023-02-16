'''
Write a program that prompts for a file name, then opens that file and reads through the file, and print the contents of the file in upper case. 
'''

fname = "words.txt"
fh = open(fname)
for a in fh:
    a = a.strip()
    a = a.upper()
    print(a)
