# Open a file

file = open ("/home/ecastillo/Downloads/seaslug.txt", mode = "r")

# print import
print (file.read())

# check whether file is closed
print (file.closed)

# Close file
file.close()

# check whether file is closed
print (file.closed)

