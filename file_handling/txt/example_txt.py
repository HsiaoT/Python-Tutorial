


# Open a text file and read all the file
fh = open("hello.txt", "r")
res1 = fh.read()
print(res1)
fh.close()

print("\n ================== \n")

# read one line at a time
fh = open("hello.txt", "r")
res2 = fh.readlines()
print(res2)
fh.close()


print("\n ================== \n")

# read one line at a time
fh = open("hello.txt", "w")
text_lines = ["first line\n", "second line\n", "third line\n"]
fh.writelines(text_lines)
fh.close()

print("\n ================== \n")
# append a file
fh = open("hello.txt", "a")
fh.write("line append...")
fh.close()