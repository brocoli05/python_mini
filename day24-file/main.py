## Read
# file = open("my_file.txt")
# contents = file.read()
# print(contents)   
# file.close()   # close the file to free up memory

# with: manage the file directly, no need to close the file
# with open("my_file.txt") as file:
#    contents = file.read()
#    print(contents)


## Write
# mode="w": overwrite
# mode="a": append
with open("my_file.txt", mode="a") as file:
   file.write("\nNew text.")