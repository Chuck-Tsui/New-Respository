'''
Write a program that prompts for a file name, then opens that file and 
reads through the file, looking for lines of the form:
X-DSPAM-Confidence:    0.8475

Count these lines and extract the floating point values from each of the lines
and compute the average of those values and produce an output as shown below. 
Do not use the sum() function or a variable named sum in your solution.
'''

fname = "file_exercise02.txt"
fh = open(fname)
count = 0
total = 0
for n in fh:
    if n.startswith("X-DSPAM-Confidence:"):
        count+=1
        a = n.find(":")
        b = n[a+1::]
        b = float(b)
        total=total+b
avg = total/count
print("Average spam confidence: "+ str(avg)) 