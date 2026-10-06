str="hello my friend"
print(str)

# multiline strings
str1="""hello"""
print(str1)

str2='''sam'''
print(str2)

s = "my name is \"rani\" from \'gulbarga\' studing in \'''kodnest\'''!"
print(s)

# Inbuilt String Methods – Single Program
s = "  kodNest Technologies 123  "


print("Original String:", s) #  kodNest Technologies 123  


# Case conversion methods
print("upper():", s.upper()) # KODNEST TECNOLOGIES 123
print("lower():", s.lower()) #  KODNEST TECHNOLOGIES 123 
print("capitalize():", s.capitalize()) # kodnest technologies 123
print("title():", s.title()) #  Kodnest Technologies 123
print("swapcase():", s.swapcase()) # kodNest Technologies 123


# Searching & counting
print("find('Tech'):", s.find("Tech")) # 10
print("count('o'):", s.count("o")) #3


# Replace
print("replace('123', '2025'):", s.replace("123", "2025"))
# kodnest technologies 2025


# Start & End check
print("startswith('  kod'):", s.startswith("  kod")) # True
print("endswith('123  '):", s.endswith("123  ")) # True


# Split & Join
words = s.split() #
print("split():", words)
print("join():", "-".join(words)) # 


# Strip spaces
print("strip():", s.strip()) #
print("lstrip():", s.lstrip())# 
print("rstrip():", s.rstrip())#  


# Checking methods
print("isalpha():", s.isalpha())# False
print("isdigit():", s.isdigit())# False
print("isspace():",s.isspace())# False
print("isalnum():", s.isalnum())# True
print("Hello".isalnum()) # True


# Length
print("Length of string:", len(s))

s1 = "hello world"
print(id(s1))
print(s1)

s1 = "hello"
print(id(s1))
print(s1)
s1 = (s1 + "world")
print(s1)
print(id(s1))

s1 = "hello"
s2 = s1 + "world"
print(id(s1),s1)
print(id(s2),s2)

s1 = "hello"
s2 = "hello"
print(id(s1),s1)
print(id(s2),s2)
print(s1 == s2)
print(s2 is s2)

#SLICING

# ============================================================

# STRING SLICING - POSITIVE SLICING PRACTICE

# ============================================================

#

# Syntax:

# string[start:stop:step]

#

# Rules:

# 1. start is included

# 2. stop is excluded

# 3. positive step moves from left to right

# 4. If step is not given, default step is 1

#

# Try to predict the output before running each question.

# ============================================================





# ------------------------------------------------------------

# LEVEL 1 - BASIC start:stop

# ------------------------------------------------------------



# 1. Extract the first 3 characters

text = "Python"
print(text[0:3])#pyt

# 2. Extract characters from index 1 to 4

text = "Programming"
print(text[1:5])#rogr

# 3. Extract characters from index 2 to 5

text = "Developer"
print(text[2:6])#velop

# 4. Extract characters from index 3 to 6

text = "Computer"
print(text[3:7])#pute

# 5. Extract the first 4 characters

text = "Artificial"
print(text[0:4])#Arti

# 6. Extract characters from index 2 to 6

text = "Education"
print(text[2:7])#ucatio

# 7. Extract characters from index 4 to 9

text = "JavaScript"
print(text[4:10])#scr

# 8. Extract characters from index 4 to 9

text = "DataScience"
print(text[4:10])#scr

# ------------------------------------------------------------

# LEVEL 2 - MISSING START OR STOP

# ------------------------------------------------------------



# 9. Extract from beginning to index 5

text = "PythonProgramming"
print(text[:6])#Python

# 10. Extract from index 6 to the end

text = "PythonProgramming"
print(text[6:])#Programming

# 11. Extract from beginning to index 8

text = "FullStackDeveloper"
print(text[:9])#FullStac

# 12. Extract from index 9 to the end

text = "FullStackDeveloper"
print(text[9:])#Developer

# 13. Extract from beginning to index 6

text = "MachineLearning"
print(text[:7])#machine

# 14. Extract from index 7 to the end

text = "MachineLearning"
print(text[7:])#learning





# ------------------------------------------------------------

# LEVEL 3 - POSITIVE STEP

# ------------------------------------------------------------



# 15. Take every second character

text = "ABCDEFGHIJ"
print(text[0:8:2])#acegi

# 16. Take every second character

text = "ABCDEFGHIJ"
print(text[1:9:2])#BDFHJ

# 17. Take every third character

text = "ABCDEFGHIJKL"
print(text[0:12:3])#adgjm

# 18. Take every second character

text = "ABCDEFGHIJKL"
print(text[2:10:2])#cegi

# 19. Take every second number

text = "1234567890"
print(text[0:10:2])#24680

# 20. Take every second number starting from index 1

text = "1234567890"
print(text[1:9:2])#24680

# ------------------------------------------------------------

# LEVEL 4 - TRICKY POSITIVE SLICING

# ------------------------------------------------------------

# 21. Take every third character

text = "Programming"
print(text[0:11:3])#Pormi


# 22. Take every third character starting from index 1

text = "Programming"
print(text[1:10:3])#roag





# 23. Take every second character

text = "PythonProgramming"
print(text[2:14:2])#thrgmir


# 24. Take every third character

text = "PythonProgramming"
print(text[1:15:3])#yhnrnm

# 25. Take every second character

text = "ABCDEFGHIJKLMNO"
print(text[3:13:2])#DFHJLN

# 26. Take every third character

text = "ABCDEFGHIJKLMNO"
print(text[2:14:3])#CFIL

# ------------------------------------------------------------

# LEVEL 5 - INTERVIEW STYLE

# ------------------------------------------------------------

# 27. Predict the output

text = "PythonProgramming"
print(text[0:16:4])#Pti

# 28. Predict the output

text = "ABCDEFGHIJKLM"
print(text[1:12:3])#BEHIK

# 29. Predict the output

text = "DataScienceWithPython"
print(text[4:18:2])#SceWitv

# 30. Predict the output

text = "FullStackDevelopment"
print(text[2:19:3])#LtaDlv

# ------------------------------------------------------------

# CONCEPT QUESTIONS

# ------------------------------------------------------------
# 31. Compare the following

text = "Python"
print(text[1:5])
print(text[1:5:1])
print(text[1:5:2])

# 32. What happens when start > stop?
text = "Python"
print(text[4:2])

# 33. What happens when start == stop?
text = "Python"
print(text[2:2])

# 34. What happens when indexes are outside the string?
text = "Python"
print(text[10:20])

# 35. What happens when stop is larger than the string length?
text = "Python"
print(text[0:100])

# ------------------------------------------------------------

# BONUS CHALLENGES

# ------------------------------------------------------------

# 36. Predict the output

text = "ABCDEFGHIJKLM"
print(text[2:11:3])

# 37. Predict the output
text = "ProgrammingLanguage"
print(text[3:15:2])

# 38. Predict the output
text = "PythonDeveloper"
print(text[1:12:3])

# 39. Predict the output

text = "DataScience"
print(text[0:10:2])

# 40. Predict the output

text = "FullStackDeveloper"
print(text[4:16:2])

#negative sliceing

s = 'python'
print(s[-5:-2:-1])