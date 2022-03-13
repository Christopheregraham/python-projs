

def main():
    points = 0
    # question 1
    answer = input("What does CPU stand for? ")
    if answer.lower() == "central processing unit":
        print('Correct!') 
        points += 1
    else:
        print('Incorrect')
    
    print("Current Score: ", points)

    # question 2
    answer = input("What does GPU stand for? ")
    if answer.lower() == "graphics processing unit":
        print('Correct!') 
        points += 1
    else:
        print('Incorrect')
    
    print("Current Score: ", points)

    # question 3
    answer = input("What does PCU stand for? ")
    if answer.lower() == "power control unit":
        print('Correct!') 
        points += 1
    else:
        print('Incorrect')
    
    print("Current Score: ", points)

    # question 4
    answer = input("What does US stand for? ")
    if answer.lower() == "united states":
        print('Correct!') 
        points += 1
    else:
        print('Incorrect')
    
    print("Current Score: ", points)

    if points >= 4:
        print("Perfect Score! " + "You've answered " + str(points) + " correctly!")
    else:
        print("Great job! You've answered " + str(points) + " correctly!")
    

print("Welcome to my quiz game!")

player = input("Do you want to play? ")


if player.lower() == "yes":
    main()
else:
    quit()


player = input("Do you want to play again? ")

if player.lower() == "yes":
    main()
else:
    quit()

print("Alright We are finished!")


    
