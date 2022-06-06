print("welcome to my computer quiz!")

playing= input("do you want to play? ")

print(playing) #prints the yes/n0

# if didnt type "yess" we have to end the program 
#text="Helo World"
#print(text.lower())

if playing.lower()!="yes":
    quit()

print("Okay lets play!") #if yes works this prints

score=0

answer=input("what is does cpu stands for? ")
if answer.lower()=="central processing unit":
    print("Correct!")
    score+=1
else:
    print("Incorrect! ")

answer=input("what is does gpu stands for? ")
if answer.lower()=="graphics processing unit":
    print("Correct!")
    score+=1
else:
    print("Incorrect! ")

answer=input("what is does RAM stands for? ")
if answer.lower()=="random access memory":
    print("Correct!")
    score+=1
else:
    print("Incorrect! ")


answer=input("what is does psu stands for? ")
if answer.lower()=="power supply unit":
    print("Correct!")
    score+=1 
else:
    print("Incorrect! ")


print("You got "+ str(score)+" questions are correct! ")
print("You got "+ str((score/4)*100)+" % ")