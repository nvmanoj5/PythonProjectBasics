from _pyrepl import reader

file = open("test.txt")
#Read all the contents of file

print(file.read())
print("-------------1")
file.close()

file1 = open("test.txt")

print(file1.read(6))
print("-------------2")
file1.close()

file2 = open("test.txt")

print(file2.readline())
print(file2.readline())
print("-------------3")
file2.close()


file3 = open("test.txt")

for line in file3:
    print(line)
    #print(file3.readline())

file3.close()
print("-------------4")

file4 = open("test.txt")
line = file4.readline()
while line!="":
    print(line)
    line = file4.readline()

file4.close()
print("-------------5")

# readlines
file5 = open("test.txt")
for line in file5.readlines():
    print(line)
file5.close()

print("------ Write ----")

with open("test.txt", "r") as reader: # If you mention this line then no need mention the close file line
    content = reader.readlines()
    reversed(content)
    with open('write.txt','w') as writer:
        for line in reversed(content):
            writer.write(line)


