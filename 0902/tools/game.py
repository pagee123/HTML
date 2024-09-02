import random
def guess_num():
    min=1
    max=100
    count=0
    target=random.randint(min, max)
    while(True):
        count+=1
        print()
        keyin = int(input(f"Guess the range of numbers: {min} - {max}: "))
        if(keyin >= min) and (keyin <= max):
            if(keyin == target):
                print(f"Bingo~ You guess it : {target}")
                print(f"You guess {count} times")
                break
            elif (keyin>target):
                max=keyin
                print("smaller")
            elif(keyin<target):
                min=keyin
                print("bigger")
            print(f"you have guesses {count} times")
        else:
            print(f"Please enter a number within the suggest range {min} - {max}")
