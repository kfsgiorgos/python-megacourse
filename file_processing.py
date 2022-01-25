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





