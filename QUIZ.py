print("WELCOME MY COMPUTER QUIZ")
playing=input("Do You Want To Play")
if (playing.lower()!="yes"):
    quit()
else:
    print("Ok Let's play")
score=0

answer=input("WHAT DOES CPU STANDS FOR ?")
if answer.lower()=="central processing unit":
    print("correct")
    score+=1
else:
    print("incorrect")
answer=input("WHAT DOES RAM STANDS FOR ?")
if answer.lower()=="random access memory":
    print("correct")
    score+=1
else:
    print("incorrect")
answer=input("WHAT DOES ROM STANDS FOR")
if answer.lower()=="read only memory":
    print("correct")
    score+=1
else:
    print("incorrect")
answer=input("WHAT DOES SMPS STANDS FOR")
if answer.lower()=="switch mode power supply":
    print("correct")
    score+=1
else:
    print("incorrect")
answer=input("WHAT DOES OS STANDS FOR")
if answer.lower()=="operating system":
    print("correct")
    score+=1
else:
    print("incorrect")
answer=input("WHAT IS THE FULL FROM OF KB")
if answer.lower()=="kilobyte":
    print("correct")
    score+=1
else:
    print("incorrect")
print("you got" + str(score) + " questions correct ")
print("you got "+ str((score/5)*100) +"%")