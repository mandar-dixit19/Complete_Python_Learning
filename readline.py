# open the file
import os


f = open("one.txt", "r")

# read the file
print(f.read())

# read the file line by line
data1 = f.readline()
print(data1)

# write operation 
# when the write operation is happen the data in the text file if replace by the data given by the write operation


# write operation is override the textand add the new data

f = open("one.txt", "w")
f.write("this is the new data \n in the file") 

f.close()

# append at the last in a existing file
 # want to on the new  line

f = open("one.txt", "a")
f.write(" \n this is the new data \n in the file")


f.close()


# # for making the new file use x this made a one txt file and  the file name is sample.txt and write dta in the file
# f = open("sample.txt", "x")
# f.write("this is a sample text")
# f.close()


# 1 r+
f = open("one.txt", "r+")
f.write("123")
print(f.read())

f.close()

# here the firdt char are replaced by the 123 from the starting
# op => 123s is the new data 
#  in the file 
#  this is the new data 
#  in the file



f = open("one.txt", "a+")
f.write("123")
print(f.read())

f.close()

# this  is the op text is going to the last
# read nahi hoga cuse the pointer at the end of the file age empty he
# 123s is the new data 
#  in the file 
#  this is the new data 
#  in the file123


#3 
f = open("one.txt", "w+")
f.write("123")
print(f.read())

f.close()
# 123 this  is the op because the write operation is override the data in the file and add the new data in the file and then read the file



# with keyword
with open("new.txt", "r") as f:
   data = f.read()
   print(len(data))

# here the f iss the object is created 
# use => when we use open and  close file there is happen to error so with is used   
  


# deleting the file so there is delete the sile one.txt
# use os module
os.remove("one.txt")