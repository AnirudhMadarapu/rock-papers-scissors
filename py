# rock-papers-scissors
#Hi, I just wrote a code to play rock, papers, scissors


import random


def computer():
    list = ['rock','scissors','paper']
    computer_choice = random.choice(list)
    ask = input("Whom should I face today?")
    inpt = ''

    while inpt != computer_choice and inpt == '':
        inpt = input(f'Hi {ask}, which one you want: scissors(s), paper(p), or rock(r): ')
        if computer_choice == list[0]:
            if inpt == 's':
              print(f"you lost the computer choice was {computer_choice}")
            elif inpt == 'p':
                print(f"you won the computer choice was {computer_choice}")
            if inpt == 'r':
                print(f"It's a tie, the computer choose {computer_choice} too")

        if computer_choice == list[1]:
            if inpt == 'p':
              print(f"you lost the computer's choice was {computer_choice}")
            elif inpt == 'r':
                print(f"you won the computer choice was {computer_choice}")
            if inpt == 's':
                print(f"It's a tie, the computer choose {computer_choice} too")
        if computer_choice == list[2]:
            if inpt == 'r':
                print(f"you lost the computer choice was {computer_choice}")
            elif inpt == 's':
                print(f"you won the computer choice was {computer_choice}")
            if inpt == 'p':
                print(f"It's a tie, the computer choose {computer_choice} too")


computer()
