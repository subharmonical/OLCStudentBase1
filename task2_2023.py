'''
A 2-player game is being programmed.
The following program allows each player, in turn, to enter the names of 5 animals. 
It converts the name of each animal to lower case. 
Each animal entered by player 2 is their guess for the animal entered by player1.
'''

#num_of_animals = 5
#for x in range(num_of_animals):
#p1_animal = input("Player 1, please enter an animal: ")
 # p1_animal = p1_animal.lower()
 # p2_guess = input("Player 2, please enter your guess: ")
  #p2_guess = p2_guess.lower() 

'''
# Open the file ANIMALGAME.py
# Save the file as ANIMAL_2023_<your name>_<centre number>_<index number>.py

#######################
Question 1: 
6.	Edit the program to allow player 1 to keep entering animals until that player 
does not want to enter any more. All animals entered by player 1 must 
be stored in a list. 

Once all animals have been entered by player 1, player 2 will enter a single guess. 

All inputs and outputs must have suitable messages. 

Save your program. 
'''
p1_animals = []

#while True:
  #p1_animal = input("player 1 pls enter an animal, type 'done' to finish").lower()
  #if p1_animal == 'done':
  #  break
 # p1_animals.append(p1_animal)

#print("player 1 has finished entering the animals: ")

##player 2 mnakes guess
#p2_guess = input("player 2, pls enter ur guess: ").lower()

#output
#print("animals entered by player1:", p1_animals)
#print("player 2 guessed:", p2_guess)
  


'''
#######################
Question 2:
7.	Save your program as ANIMAL2_2023_<your name>_<centre number>_<index number>.py [3 marks]

Edit your program to search the list of animals to find the guess 
entered by player 2. 
Player 2 has a score that starts at 0. 
If the guess entered by player 2 is found in the list:

> the animal is removed from the list
> the score for player 2 is incremented by 1

Save your program.
########################
'''
#while True:
 # p1_animal = input("player 1 pls enter an animal, type 'done' to finish: ").lower()
 # if p1_animal == 'done':
 #   break
 # p1_animals.append(p1_animal)

#print("player 1 has finished entering the animals: ")

#score 
#p2_score = 0
#p2_guess = input("player 2, pls enter ur guess: ").lower()

#if p2_guess in  p1_animals:
 # p1_animals.remove(p2_guess)
 # p2_score += 1
 # print("correct guess!", p2_guess, "was in the list")
#else:
 # print("wrong guess!", p2_guess, "was not in the list")

#print("remaining animals in the list are:", p1_animals)


'''
Question 3:
8.	Save your program as ANIMAL3_2023_<your name>_<centre number>_<index number>.py

Edit your program to allow player 2 to keep entering guesses until they 
enter an animal that is not found in the list, or until the list is empty. 
When player 2 enters an animal that is not found in the list:

> the game ends and informs player 2 the game is over
> a message is displayed showing:
- player 2 their score
- the animals that are still in the list.

All inputs and outputs must have suitable messages.
Save your program.

[3 marks]
'''
p1_animals = []

while True:
  p1_animal = input("player 1 pls enter an animal, type 'done' to finish: ").lower()
  if p1_animal == 'done':
    break
  p1_animals.append(p1_animal)

print("player 1 has finished entering the animals: ")

#score
p2_score = 0

while p1_animals:
  p2_guess = input("player 2 pls enter ur guess: ").lower()

  if p2_guess in  p1_animals:
    p1_animals.remove(p2_guess)
    p2_score += 1
    print("correct guess!", p2_guess, "was in the list")
  else:
    print("wrong guess!", p2_guess, "was not in the list")
    break
  
if not p1_animals:
  print("the list of animals is now empty")

print("game over. player 2's final score is:", p2_score)
print("remaining animals in the list:", p1_animals)