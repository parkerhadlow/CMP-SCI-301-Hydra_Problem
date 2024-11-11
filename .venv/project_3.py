#set game to active to enter the loop
game_over = False
while not game_over:
    #take the initial head value from the user. assume an invalid input.
    valid_head_amt = False
    while not valid_head_amt:
        head_amt = input("Number of heads:")
        if head_amt.isnumeric():
            head_amt = int(head_amt)
            if head_amt >= 0:
                valid_head_amt = True
                #store the initial head quantity for the CPU to use later
                head_num = head_amt
            else:
                print(f'Please enter a numerical value greater than 0.')
        else:
            print(f'Please enter a numerical value greater than 0.')
    #take the initial head value. assume an invalid input.
    valid_tail_amt = False
    while not valid_tail_amt:
        tail_amt = input("Number of tails:")
        if tail_amt.isnumeric():
            tail_amt = int(tail_amt)
            if tail_amt >= 0:
                valid_tail_amt = True
                #store the initial tail quantity for the CPU to use later
                tail_num = tail_amt
            else:
                print(f'Please enter a numerical value greater than 0.')
        else:
            print(f'Please enter a numerical value greater than 0.')
    #set a variable to show what move the player is on
    move_number = 1
    #enter a loop that allows the user to make moves until there are no more heads and tails
    while head_amt != 0 or tail_amt != 0:
        #set variable for input interpretation
        valid_move = False
        #user selects what move to use
        while not valid_move:
            move = input(f'Move {move_number}:')
            if move.isdigit():
                move = int(move)
                if move >= 1 and move <= 5:
                    valid_move = True
                    if move == 1:
                        if head_amt < 1:
                            valid_move = False
                            print(f'This is not a valid move. Hydra now has {head_amt} heads and {tail_amt} tails.')
                    elif move == 2:
                        if tail_amt < 1:
                            valid_move = False
                            print(f'This is not a valid move. Hydra now has {head_amt} heads and {tail_amt} tails.')
                    elif move == 3:
                        if head_amt < 2:
                            valid_move = False
                            print(f'This is not a valid move. Hydra now has {head_amt} heads and {tail_amt} tails.')
                    elif move == 4:
                        if tail_amt < 2:
                            valid_move = False
                            print(f'This is not a valid move. Hydra now has {head_amt} heads and {tail_amt} tails.')
                else:
                    print(f'This is not a valid move. Hydra now has {head_amt} heads and {tail_amt} tails.')
            else:
                print(f'This is not a valid move. Hydra now has {head_amt} heads and {tail_amt} tails.')
        if move == 1:
            #remove one head and grow one back
            head_amt -= 1
            head_amt += 1
            print(f'Use the first move.', end='')
        elif move == 2:
            #remove one tail and grow two back
            tail_amt -= 1
            tail_amt += 2
            print(f'Use the second move.', end='')
        elif move == 3:
            #remove two heads
            head_amt -= 2
            print(f'Use the third move.', end='')
        elif move == 4:
            #remove two tails and grow one head
            tail_amt -= 2
            head_amt += 1
            print(f'Use the fourth move.', end='')
        #if the hydra is not dead, add one to the move counter
        if head_amt != 0 or tail_amt != 0:
            move_number += 1
        print(f' The Hydra now has {head_amt} heads and {tail_amt} tails.')
    print(f'Congratulations! You killed the Hydra in {move_number} moves.')
    # ask the user to play again
    # set placeholder
    play_again = ''
    # enter loop to collect proper input
    while play_again != 'y' and play_again != 'n':
        play_again = input('Would you like to play again? (y/n):')
        if play_again != 'y' and play_again != 'n':
            print('Please enter y or n.')
        # continue the game if they enter y
        elif play_again == 'y':
            game_over = False
        # end the game if they enter n
        else:
            game_over = True

