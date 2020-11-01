from random import randint
with open("words.txt","r") as words:
    words_file = words.read().split("\n")
index = randint(0,len(words_file))
word = words_file[index]
guess_list = []
name = input("Enter your name: ")
print("Welcome " + name + " to play hangman!")
if len(word) > 5:
    lives = 20
else:
    lives = 10

while lives >0:
    checkpoint = len(word)
    for letter in word:
        if letter in guess_list:
            print(letter)
            checkpoint -= 1
        else:
            print("*")
    if checkpoint ==0:
        print("You won!")
        break
    guess = input("Give a letter: ")
    guess_list += guess
    if guess not in word:
        print("Wrong letter try again!")
        lives -=1
        if lives !=0:
            print(f"You have {lives} left")
    if lives == 0:
        print("Game over!")
