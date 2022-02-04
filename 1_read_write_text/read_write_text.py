#We need to read and write text data.
#So, you should understand how to handle text files.

#Q. What's the purpose of this program?

f = open("sample.txt", "r")
lines= f.read().splitlines()
f.close()

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

f = open("output.txt", "w")
f.write(message)
f.close()
