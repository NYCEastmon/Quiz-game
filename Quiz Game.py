#Quiz Game 

print("Welcome to Malcolm's Quiz Game\n")

#User decides if they want to play.

playing = input("Do you want to play?\n")

if playing.lower() != "yes" :
    quit()
    
print("Great let's play!\n")    

#This varible will store the users score 
score = 0

#Question 1

answer = input("What is the captial of The United States?\n ")

if answer.lower() == "washington d.c" :
    print("Correct!")
    score += 1
    
else:
    print("Incorrect")
    
#Question 2
    
answer = input("Where is the Grand Canyon?\n ")

if answer.lower() == "arizona" :
    print("Correct!")
    score += 1
    
else:
    print("Incorrect")
    
#Question 3
   
answer = input("What city is called the big apple?\n" ) 

if answer.lower() == "new york city" :
    print("Correct!")
    score += 1
    
else:
    print("Incorrect")    
    
#Question 4
    
answer = input("Who was the 44th president of the united states?\n"  ) 

if answer.lower() == "barack obama" :
    print("Correct!")
    score += 1
    
else:
    print("Incorrect")     
    
print("You got " + str(score) + " questions correct")    