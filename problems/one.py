# # problem no 1
# # open the file in write mode
# with open("name.txt", "w") as f:
#   # give the 5 nme for the input
#   for i in range(5):
#     name = input("enter the name :")
#     f.write(name + "\n")
# with open("name.txt", "r") as f:
#   data = f.read()
#   print(data)


# # problem no 2
# with open("log.txt", "a") as f:
#   log = input("enter the log:")
#   f.write(log + "\n") 


# with open("log.txt", "r") as f:
#   data = f.read()
#   print(data)   


# problem no 3
L = [5,10,15,20,25]
L = [num for num in L if num > 15]
print(L)