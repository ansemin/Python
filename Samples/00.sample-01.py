from ast import While
import random

random_number=random.randint(1,100)

#print(random_number)

game_count=1

while True:


        my_number=int(input("Choose number between 1_100"))

        if my_number>random_number:
            print('Down')
        elif my_number<random_number:
            print("Up")
        else:
            print(f'Congrat, you won in {game_count}tries')
            break
        game_count=game_count+1    