import random

answerlist=["world","look","hello","goodbye"]

random.shuffle(answerlist)

answer=list(answerlist[0])



display=[]
used=[]

display.extend(answer)
used.extend(answer)


for i in range(len(display)):

    display[i]="_"


print(' '.join(display))

count=0

incorrect=5

while count<len(answer) and incorrect>0:
    guess=input("Please guess a letter : ")
    guess=guess.lower()
    print(count)


    for i in range(len(answer)):
        if answer[i]==guess and guess in used:
            display[i]=guess
            count=count+1
            used.remove(guess)

    if guess not in display:
        incorrect =incorrect-1
        print("Sorry wrong guess.You have",incorrect,"chances left")


    print(' '.join(display))



if count==len(answer):
    print("You won the game")

else:
    print("Game is Over")
    print(answer)
