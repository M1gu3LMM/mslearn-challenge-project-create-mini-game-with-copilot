# write 'hello world' to the console
print('hello world')

# show a menu with explain the options: play, exit to the console
print('\n1. Play')
print('\n2. Exit')
# get the user input
choice = input('Enter your choice: ')

# if the user input is 1, print 'You chose to play' and show the game menu, the player can choose: rock, paper, scissors
# the user has to enter the string 'rock', 'paper', 'scissors' to play the game

# create a variable for the player score and the number of games played
player_score = 0
games_played = 0


# make that the player can play the game multiple times without restarting the program, use a loop while True and break the loop if the user input is 2

if choice == '1':
    while True:
        print('You chose to play')
        print('\n- rock')
        print('\n- paper')
        print('\n- scissors')
        print('\n- exit')
        player_choice = input('Enter your choice: ')
        # generate the computer choice randomly
        import random
        computer_choice = random.choice(['rock', 'paper', 'scissors'])
        # if invalid choice, don´t show the computer choice
        if player_choice in ['rock', 'paper', 'scissors']:
                print(f'Computer chose {computer_choice}')
        # if the player choice is the same as the computer choice, print 'It is a draw'
        if player_choice == computer_choice:
            print('It is a draw')
        # if the player choice is 'rock' and the computer choice is 'scissors', print 'You win'
        elif player_choice == 'rock' and computer_choice == 'scissors':
            print('You win')
            # if the player wins, increase the player score by 1
            player_score += 1
        # if the player choice is 'rock' and the computer choice is 'paper', print 'You lose'
        elif player_choice == 'rock' and computer_choice == 'paper':
            print('You lose')
        # if the player choice is 'paper' and the computer choice is 'rock', print 'You win'
        elif player_choice == 'paper' and computer_choice == 'rock':
            print('You win')
            # if the player wins, increase the player score by 1
            player_score += 1
        # if the player choice is 'paper' and the computer choice is 'scissors', print 'You lose'
        elif player_choice == 'paper' and computer_choice == 'scissors':
            print('You lose')
        # if the player choice is 'scissors' and the computer choice is 'paper', print 'You win'
        elif player_choice == 'scissors' and computer_choice == 'paper':
            print('You win')
            # if the player wins, increase the player score by 1
            player_score += 1
        # if the player choice is 'scissors' and the computer choice is 'rock', print 'You lose'
        elif player_choice == 'scissors' and computer_choice == 'rock':
            print('You lose')
        # if the player choice is not 'rock', 'paper', 'scissors', print 'Invalid choice'
        #exit to the loop
        elif player_choice == 'Exit' or player_choice == 'exit' or player_choice == 'EXIT':
            print('You chose to exit')
            # show the score of the player and the number of games played
            print(f'Player score: {player_score}')
            print(f'Games played: {games_played}')
            
            
            break
        else:
            print('Invalid choice')
        # increase the number of games played by 1
        games_played += 1
# if the user input is 2, print 'You chose to exit' and exit the program
elif choice == '2':
    print('You chose to exit')
    exit()  # exit the program

# if the user input is not 1 or 2, print 'Invalid choice'
else:
    print('Invalid choice')
