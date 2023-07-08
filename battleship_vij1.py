"""
Author: Aryan Vij, vij1@purdue.edu
Assignment: 12.1 - Battleship
Date: 6/26/2023

Description:
    Create a space themed single player variation of Battleship. This is a classic guessing game
dating back to the 1930s in which players try to shoot enemy ships in a ten-by-ten grid by
guessing grid coordinates.

Contributors:
    Aryan Vij, vij1@purdue.edu [repeat for each]

My contributor(s) helped me:
    [ ] understand the assignment expectations without
        telling me how they will approach it.
    [ ] understand different ways to think about a solution
        without helping me plan my solution.
    [ ] think through the meaning of a specific error or
        bug present in my code without looking at my code.
    Note that if you helped somebody else with their code, you
    have to list that person as a contributor.

Academic Integrity Statement:
    I have not used source code obtained from any unauthorized
    source, either modified or unmodified; nor have I provided
    another student access to my code.  The project I am
    submitting is my own original work.
"""

"""Import additional modules below this line (starting with unit 6)."""


"""Write new functions below this line (starting with unit 4)."""


import random
from urllib.request import HTTPPasswordMgrWithDefaultRealm
import numpy as np

def menu():
    print("\nMenu:")
    print("  1 : Instructions")
    print("  2 : View Example Map")
    print("  3 : New Game")
    print("  4 : Hall of Fame")
    print("  5 : Quit")

def instructions():
    print("Instructions: \n") 

    print("Ships are positioned at fixed locations in a 10-by-10"
        +"\ngrid.  The rows of the grid are labeled A through J, and"
        +"\nthe columns are labeled 0 through 9.  Use menu option"
        +"\n2 to see an example.  Target the ships by entering the"
        +"\nrow and column of the location you wish to shoot.  A"
        +"\nship is destroyed when all of the spaces it fills have"
        +"\nbeen hit.  Try to destroy the fleet with as few shots as"
        +"\npossible. The fleet consists of the following 5 ships:\n"
        )
    print("Size : Type:")
    print("   5 : Mothership")
    print("   4 : Battleship")
    print("   3 : Destroyer")
    print("   3 : Stealth Ship")
    print("   2 : Patrol Ship")

#This function should take no argu- 
#ments and return the grid as a list of ten nested lists, with 10 elements each.
def make_grid():
    nested_list = [
        ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
        ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
        ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
        ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
        ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
        ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
        ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
        ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
        ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
        ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
    ]
    #Mother Ship
    while True:
        x = random.randint(0,9)
        y = random.randint(0,9)
        if x != 0 and x != 9 and y != 0 and y != 9:
            if nested_list[x][y] == '~' and nested_list[x-1][y] == '~' and nested_list[x+1][y] == '~' and nested_list[x][y+1] == '~' and nested_list[x][y-1] == "~":
                nested_list[x][y] = "M"
                nested_list[x - 1][y] = "M"
                nested_list[x + 1][y] = "M"
                nested_list[x][y + 1] = "M"
                nested_list[x][y - 1] = "M"
                break
    #Battle Ship
    while True:
        x = random.randint(0,9)
        y = random.randint(0,9)
        if x != 9 and y != 9:
            if nested_list[x][y] == "~" and nested_list[x+1][y] == "~" and nested_list[x][y+1] == "~" and nested_list[x+1][y+1] == "~":
                nested_list[x][y] = "B"
                nested_list[x + 1][y] = "B"
                nested_list[x][y + 1] = "B"
                nested_list[x + 1][y + 1] = "B"
                break
    #Destroyer Ship
    while True:
        x = random.randint(0,9)
        y = random.randint(0,9)
        if x != 9 and y != 9:
            #randomly throws error here
            if nested_list[x][y] == "~" and nested_list[x+1][y] == "~" and nested_list[x][y+1] == "~":
                nested_list[x][y] = "D"
                nested_list[x + 1][y] = "D"
                nested_list[x][y + 1] = "D"
                break
    #Stealth Ship
    while True:
        x = random.randint(0,9)
        y = random.randint(0,9)
        if y != 0 and y != 9:
            if nested_list[x][y] == "~" and nested_list[x][y-1] == "~" and nested_list[x][y+1] == "~":
                nested_list[x][y] = "S"
                nested_list[x][y + 1] = "S"
                nested_list[x][y - 1] = "S"
                break
    #Patrol Ship
    while True:
        x = random.randint(0,9)
        y = random.randint(0,8)
        if nested_list[x][y] == "~" and nested_list[x][y+1] == "~":
            nested_list[x][y] = "P"
            nested_list[x][y + 1] = "P"
            break

    return nested_list

def hof_add_user(name, hit_count, miss_count):
    existing_accuracies, existing_names = hof_data()

    existing_names.append(name)
    existing_accuracies.append(1700 / (17 + miss_count))

    with open("battleship_hof.txt", "w") as f:
        f.write("name,hits,misses\n") #reinsert the header

        for i in range(len(existing_accuracies)):
            name = existing_names[i]
            hit_count = 17
            miss_count = ((hit_count * 100) / existing_accuracies[i]) - hit_count
            f.write(f'{name},{hit_count},{miss_count:.0f}\n')


    # calculate all of the misses and put them into a list and write that list line by line to the file
    #if (len(existing_names) == 10): #for later

def accuracy_check(accuracy):
    accuracies, names = hof_data()
    if len(accuracies) < 10:
        return True
    sorted(accuracies)
    if accuracy < accuracies[9]:
        return False
    
    return True
    
    

def hall_of_fame():
    print()
    print("~~~~~~~~ Hall of Fame ~~~~~~~~")
    print("Rank : Accuracy :  Player Name")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    accuracy, names = hof_data()


    rank = 1
    while len(accuracy) > 0 and rank <= 10:
        max_score = 0
        max_index = 0
        for index, score in enumerate(accuracy):
            if score > max_score:
                max_score = score 
                max_index = index
        print(f"{rank:4} {max_score:9.2f}%", f'{names[max_index]:>14}')
        rank += 1
        accuracy.pop(max_index),
        names.pop(max_index)
                

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    
def hof_data():
    name, hits, misses = [],[],[]
    accuracy_list = []

    with open("battleship_hof.txt") as f:
        f.readline()
        for line in f:
            line.rstrip("\n")
            hof_list = line.split(",")
    
            name.append(hof_list[0].rstrip())
            hits.append(int( float(hof_list[1].rstrip())))
            misses.append(int( float(hof_list[2].rstrip())))

    for i in range(len(name)):
        accuracy_list.append( hits[i] / (hits[i] + misses[i]) * 100 )
        
    
    return accuracy_list,name



def print_grid(user_grid):
    letters = ["A","B","C","D","E","F","G","H","I","J"]

    print(*[" ",0,1,2,3,4,5,6,7,8,9], sep= "  ")
    for i in range(len(user_grid)):
        print(*letters[i],*user_grid[i], sep= "  ")
    print()


def main():
    """Write your mainline logic below this line (then delete this line)."""
    print()
    print("               ~ Welcome to Battleship! ~               \n")
    print("ChatGPT has gone rogue and commandeered a space strike" 
        +"\nfleet. It's on a mission to take over the world.  We've"
        +"\nlocated the stolen ships, but we need your superior"
        +"\nintelligence to help us destroy them before it's too"
        +"\nlate.")
    
    
    while True:
        menu() #front menu
        choice = input("What would you like to do? ")
        print()
        if choice in ("1","2","3","4","5"):
            if choice == "1":
                instructions()
            if choice == "2":
                grid = make_grid()
                print_grid(grid)
            if choice == "3":
                letters = ["A","B","C","D","E","F","G","H","I","J"]
                numbers = ["0","1","2","3","4","5","6","7","8","9"]

                #print for now
                grid = make_grid() #actual grid

                user_grid = [
                    ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
                    ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
                    ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
                    ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
                    ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
                    ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
                    ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
                    ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
                    ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
                    ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
                ] #this is what the user can see

                #print_grid(grid) #This is for testing
                print_grid(user_grid)
                
                chosen_already = [] #if you already chose it
                letter_hit = {"M" : 0, "B" : 0, "S" : 0, "D" : 0, "P" : 0}

                miss_count = 0 #miss count

                while True:

                    target = input("Where should we target next (q to quit)? ").upper()
                    
                    if target == "Q":
                        break
                    
                    if len(target) != 2:         
                        print("Please enter exactly two characters.")
                        continue
                        

                    let = target[0] #letter
                    num = target[1] #number



                    if len(target) == 2:
                        if (let in letters) and (num in numbers):
                            if (target in chosen_already): #check if that spot was hit already
                                print("You already chose this spot. Please choose another one.")
                            else: 
                                chosen_already.append(target) #issue: replacing 

                            #used to map a letter to a number to hit the grid
                            letter_mapper = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9}

                            x = int(letter_mapper[let.upper()]) #maps the user letter to the correct number
                            y = int(num) #maps user number to the correct number

                            hit_count = 0

                            #if you miss
                            if (grid[x][y] == "~"):
                                print("\nmiss")
                                print()
                                user_grid[x][y] = "o"

                                #prints the grid

                                miss_count += 1
                                #print(miss_count)
                            
                            else:
                                
                                letter_hit[grid[x][y]] += 1 

                                print("\nIT'S A HIT!")

                                if (letter_hit["M"] == 5 and grid[x][y] == "M"):
                                    print("The enemy's Mothership has been destroyed.")
                                elif (letter_hit["B"] == 4 and grid[x][y] == "B"):
                                    print("The enemy's Battleship has been destroyed.")
                                elif (letter_hit["S"] == 3 and grid[x][y] == "S"):
                                    print("The enemy's Stealth Ship has been destroyed.")
                                elif (letter_hit["D"] == 3 and grid[x][y] == "D"):
                                    print("The enemy's Destroyer has been destroyed.")
                                elif (letter_hit["P"] == 2 and grid[x][y] == "P"):
                                    print("The enemy's Patrol Ship has been destroyed.")

                                print()

                                
                                if(letter_hit["M"] == 5 
                                    and letter_hit["B"] == 4 and letter_hit["S"] == 3 and letter_hit["D"] == 3 and letter_hit["P"] == 2):
                                    
                                    print("You've destroyed the enemy fleet!")
                                    print("Humanity has been saved from the threat of AI.")
                                    print()
                                    print("For now ...")
                                    print()
                                   

                                    is_top_ten = accuracy_check(1700/(17 + miss_count))
                                    
                                    
                                    
                                    if(is_top_ten):
                                        
                                        print("Congratulations, you have achieved a targeting accuracy")
                                        if (miss_count == 0):
                                            print(f"of 100.00% and earned a spot in the Hall of Fame.")
                                        else:
                                            print(f"of {(1700/(miss_count + 17)):.2f}% and earned a spot in the Hall of Fame.")
                                        player_name = input("Enter your name: ") #to write to file later
                                        hof_add_user(player_name, hit_count, miss_count) 
                                        print()
                                        hall_of_fame() #display the hall of fame
                                    
                                    else:
                                        print(f"Your targeting accuracy was {(1700)/(17 + miss_count):.2f}%.")

                                    break


                                user_grid[x][y] = "x"

                                hit_count +=1
                            
                            print_grid(user_grid)
                                
                        else:
                            print('Please enter a location in the form "G6".')

                        


               

            if choice == "4":
                hall_of_fame()

            if choice == "5":
                print("Goodbye")
                print()
                break
        else: 
            print("Invalid selection.  Please choose a number from the menu.")

    
    


    

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
