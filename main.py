import random

computer= random.choice([0,-1,1])

you=input("Enter your choice (r for rock, p for paper, s for scissors): ")
youdict={'r': 0, 'p': -1, 's': 1}
you= youdict[you]
reverseDict={0:'rock', -1:'paper', 1:'scissors'}    


print("Computer choice: ", reverseDict[computer])
print("Your choice: ", reverseDict[you])

if computer==you:
    print("It's a tie!")
else:
    if (computer==0 and you==1) or (computer==-1 and you==1) or (computer==1 and you==-1):
        print("You lose!")  
    else:
        print("You win!")    
