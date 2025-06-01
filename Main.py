import random
import art
import word_list
print("\n")
print("Welcome to Hangman !!\n")
print(art.stage0)
word = random.choice(word_list.word_list)
size = len(word)
blank=""
for i in range(size):
    blank += "_"
print (blank)
print("\n")

game_over = False
ans = []
no_of_lives = 7
print("You have total 7 lives !!")
while not game_over:
    player = input("Enter a character: ").lower()
    if player in ans:
        print("You have already guessed this try something different.")
    disp =""
    for text in word:
        if text == player:
            disp += text
            ans += text
        elif text in ans:
            disp += text
        else:
            disp += "_"
    if player not in word:
        no_of_lives = no_of_lives -1
        print(f"{player} is wrong. You lost a life")
    print(f"No. of Lives left : {no_of_lives}")


    if no_of_lives == 7:
        print(art.stage0)
    elif no_of_lives == 6:
        print(art.stage1)
    elif no_of_lives == 5:
        print(art.stage2)
    elif no_of_lives == 4:
        print(art.stage3)
    elif no_of_lives == 3:
        print(art.stage4)
    elif no_of_lives == 2:
        print(art.stage5)
    else:
        print(art.stage6)
        print("GAME OVER!!")
        game_over = True    
    print(disp)



    if "_" not in disp:
        game_over = True
        print("You win!!")
