print("Welcome to my computer quiz!")

playing = input("Do you want to to play? ")

if  playing.lower() != "yes":
    quit() # this the function in the python which is use to quit the program---> terminate the program


print("Okay! let`s play :)")

score = 0


answer = input("what does CPU stands for ? ")
if answer.lower() == "central processing unit":
    print("correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("what does PSU stands for ? ")
if answer.lower() == "power supply":
    print("correct!")
    score += 1
else:
    print("Incorrect!")


answer = input(" what does GPU stand for ? ")
if answer.lower() == "graphic processing unit":
    print("correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("what does RAM stand for ? ")
if answer.lower() == "random access memory":
    print("correct!")
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) +" " + "questions correct !")
print("You got " + str((score/4) *100) + " "+ " questions correct!" +  "%.") # it gives the percentage

# we cannot add a integer and string operation at the same time
# "ankit" + 1 --->that just undefined operation , we cannot do it

# "ankit" + "1'-----> we can add two strings in this manner

# example of lower
#text = "IAm is THE bESt"
#print(text.lower()) # it will convert the text in the lower case
#lower is used to convert all the text into the lower case that is the main criteria
# upper are used to convert all the text in the upper case , upper are used to convert all the text in the uppercase




