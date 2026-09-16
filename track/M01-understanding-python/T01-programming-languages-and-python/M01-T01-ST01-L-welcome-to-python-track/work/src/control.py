age = 18
if age >=18:
    print("eligible to vote")
else:
    print("not eligible to vote")

for i in range(1,6):
    print(i)

for i in range(5):
    print(i)

for i in range(2,10,2):
    print(i)

for i in range(1,11):
    if i % 2 == 0:
        print(i)

count = 1
while count<=5:
    print(count)
    count=count+1

free_tonight = True
friends_avaiable = True
if(free_tonight):
    if(friends_avaiable):
        print("go out and enjoy")
    else:
        print("seat and watch at home")
else:
    print("not avaiable for party")

day = int(input("enter a number between 1 and 7:"))
match day:
    case 1: print("monday")
    case 2: print("tuesday")
    case 3: print("wednesday")
    case 4: print("thursday")
    case 5: print("friday")
    case 6: print("saturday")
    case 7: print("sunday")
    case _: print("invalid")




    