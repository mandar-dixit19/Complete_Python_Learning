f = open("one.txt", "r")
# after opening the file file returns the file object

# read operation
data = f.read()
print(data)
print(type(data))

f.close()