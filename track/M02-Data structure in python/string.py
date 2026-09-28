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