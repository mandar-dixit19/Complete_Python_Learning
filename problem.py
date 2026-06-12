
# this is how we perfor m the opeartion
# if we wnt ro print the line no
line  = 1
data = True
word =  "python"
with open("problem.txt", "r") as f:
    while data:
     data = f.readline()
     # for founding the python word
     if word in data:
        print(f"{word} is found in line no {line}")
        break
     
     print(data)
     line += 1



    