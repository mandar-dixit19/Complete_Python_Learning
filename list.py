# list comprehension

sq = [i * i  for i in range(6) if i%2 != 0]
print(sq)


num = [-1, -2, 3,4, 5,-6]
sq = [0 if value < 0 else value for value in num]
print(sq)



words  = ["python", "java", "c++", "ruby"]
words = [val.upper() for val in words ]
print(words)