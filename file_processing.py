# a function that gets a single string character and a filepath and 
# returns the number of occurences of that character in the file.
def foo(character, filepath="bear.txt"):
    file = open(filepath)
    content = file.read()
    return content.count(character)

res = foo("p",filepath="bear.txt")
print(res)

# create  a file with name file.txt and write the text "snail" there
with open("file.txt", "w") as file:
    file.write("\nsnail")

# create a first.txt file that contains the first 90 characters of bear.txt
with open("bear.txt", "r") as file:
    content = file.read()
with open("bear_copy.txt", "w") as file:
    file.write(content[:90])


# append the text of bear1.txt to bear2.txt 
with open("bear1.txt", "r") as file:
    content = file.read()
with open("bear2.txt", "a") as file:
    file.write('\n')
    file.write(content)



#modify the content of data.txt in order to have two times its content

# Hint: Create a "with" block where you open the file in 'a+' mode. Put the cursor on top of the file. 
# Read the file storing its content in a variable, put the cursor on top of the file, write the content, 
# write the content.
with open("data.txt", "a+") as file:
    file.seek(0)
    content = file.read()
    file.seek(0)
    file.write(content)
    file.write(content)




