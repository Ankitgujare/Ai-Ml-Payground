"""
here we will see the diffrent Basic Operations which we do
In file

1Open
2.read
3.write
close the file

to open the file we use the open(filename,mode)
open functions returns the File Object
"""

f = open("sample.txt", "r")
# #read the whole file
# data = f.readline()
# data1= f.readline()
# print(data,end="")
# print(data1)


#we can aslo use loop lets try

for i in range(0,3,1):
    print(f.readline(),end="")


#we can read the files line by line

