#String concatenation

a = "Hello"
b = a +"Chuck"  # + operator applied to String
print(b)        #"HelloChuck"

# in as Logical Operator
fruit = "apple"
print("a" in fruit)    # True
print("b" in fruit)    # False

'''
python has a number of string functions in string library

find() finds the first occurrence of the substring
if the substring is not found, find() returns -1

upper() make a string in upper case
lower() make a string in lower case
replace() replaces all occurrences of the string with the replacement string

lstrip() and rstrip() remove whitespace at the left or right
strip() remove both left and right

'''

pos = fruit.find("pp")
# a|p|p|l|e
# 0|1|2|3|4
print(pos)  # 1

pos = fruit.find("x")
print(pos)   # -1


print(b.lower())    #hellochuck
print(b.upper())    #HELLOCHUCK
c = b.replace("Chuck","Joe")
print(c)            #HelloJoe
print(b)            #HelloChuck
#in above python code, why b's value do not change ?
#because the lower(), upper(), replace() string method return a new string but they do not modify the orginal string

