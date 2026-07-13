#Quiz app program
ans=input("Do you want to answer the questions?")
while True:
    if ans=='YES' or ans=='yes' or ans=='Yes':
        score=0
        One=input("What is the capital of India?").strip().lower()
        if One=='new delhi' or One=='delhi':
            print("Correct answer!")
            score+=1
        else:
            print("Wrong answer!")
        Two=input("What is the capital of Karnataka?").strip().lower()
        if Two=='banglore':
            print("Correct answer!")
            score+=1
        else:
            print("Wrong answer!")
        Three = input("Which planet is known as the Red Planet? ").strip().lower()
        if Three=='mars':
            print("Correct answer!")
            score+=1
        else:
            print("Wrong answer!")
        Four=input("How many continents are there?").strip().lower()
        if Four=='7' or Four=='seven':
            print("Correct answer!")
            score+=1
        else:
            print("Wrong answer!")
        Five=input("Which is the largest ocean on Earth?").strip().lower()
            if Five=='pacific ocean':
            print("Correct answer!")
            score+=1
        else:
            print("Wrong answer!")
        print("You scored",score,"out of 5")
        if score==5:
            print("Excellent score!")
        elif score==4:
            print("Great job!")
        elif score==3:
            print("Good effort")
        else:
            print("Keep working!")
        Quest=input("Do you want to play again?").strip().lower()
        if Quest=='no':
            break            
    else:
        print("No questions!")
        

        



    
