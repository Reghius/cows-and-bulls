import random

def number_generator():
    return random.sample(range(0, 9), 4)

def game_play():
    global turns
    bulls = 0
    cows = 0
    choose_number = input("Enter your four digit number: ")
    turns += 1
    input_number = []
    for i in range(4):
        input_number.append(int(choose_number[i]))
    for x in range(4):
        for y in range(4):
            if input_number[x] == number[y]:
                cows += 1
    for j in range(4):
        if input_number[j] == number[j]:
            bulls += 1
    print("Bulls: ", bulls)
    print("Cows: ", cows)
    if bulls == 4:
        print("You won in", turns, "turns")
    if bulls != 4:
        game_play()
    

if __name__ == '__main__':
    turns = 0
    number = number_generator()
    game_play()

