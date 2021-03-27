with open('1.txt') as file: #file 1 is in current directory
    text = file.read()

text = text.replace(' — ', '  ')#this fuction find all symbols in our file and change it
print(text)
with open('2.txt', "w") as rep_file:
    rep_file.write(text) #rewrite text in file 2

