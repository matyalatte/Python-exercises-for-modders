'''
A. Read sample.txt, count the number of lines that is 'cat', and write the result.
'''

#Read lines
f = open("sample.txt", "r")
lines= f.read().splitlines()
f.close()

#Count Cats
count=0
row=0
for line in lines:
    if line=="cat":
        count+=1
        print("I've found a cat! (" + str(row) + ")")
    row+=1

if count==0:
    message="There are no cats."
if count==1:
    message="There is a cat."
else:
    message="There are " + str(count) + " cats."

#Write the result
f = open("output.txt", "w")
f.write(message)
f.close()
