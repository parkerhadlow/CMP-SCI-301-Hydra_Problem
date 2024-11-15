#set game to active to enter the loop
game_over = False
while not game_over:
    # tell the user what the different moves are
    print(f'''
Oh no Hercules! A Hydra is quickly approaching. You must slay it! Here are your options:
Move 1: Cut off exactly one head, but another will grow in its place.
Move 2: Cut off exactly one tail, but two more will grow in its place.
Move 3: Cut off exactly two heads.
Move 4: Cut off exactly two tails, but a new head wil grow.
Move 5: Succumb to the Hydra.
    ''')

    #take the initial head value from the user. assume an invalid input.
    valid_head_amt = False
    while not valid_head_amt:
        head_amt = input("Number of heads: ")
        #if they enter a digit, make it an integer to check that it's greater than zero
        if head_amt.isdigit():
            head_amt = int(head_amt)
            #if it's a digit greater than zero, set validity to true to exit the loop
            if head_amt > 0:
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
        tail_amt = input("Number of tails: ")
        # if they enter a digit, make it an integer to check that it's greater than zero
        if tail_amt.isdigit():
            tail_amt = int(tail_amt)
            # if it's a digit greater than zero, set validity to true to exit the loop
            if tail_amt > 0:
                valid_tail_amt = True
                #store the initial tail quantity for the CPU to use later
                tail_num = tail_amt
            else:
                print(f'Please enter a numerical value greater than 0.')
        else:
            print(f'Please enter a numerical value greater than 0.')

    #set variables for the CPU to count moves
    move_count = 1
    move_list = []

 # Begin CPU computation of the most efficient way to kill the hydra
    # repeat move 2 to change the tail number until it, when divided by two,  adds to create an even sum with the head number.
    while ((tail_num / 2) + head_num) % 2 != 0:
        tail_num -= 1
        tail_num += 2
        # record the move into a list to print later
        move_list.append(
            f'Move {move_count}: Use the second move. Hydra now has {head_num} heads and {tail_num} tails.')
        move_count += 1
    # repeat move 4 until there are no tails left
    while tail_num != 0:
        tail_num -= 2
        head_num += 1
        # record the move into a list to print later
        move_list.append(
            f'Move {move_count}: Use the fourth move. Hydra now has {head_num} heads and {tail_num} tails.')
        move_count += 1
    # repeat move 3 until there are no heads left
    while head_num != 0:
        head_num -= 2
        # record the move into a list to print later
        move_list.append(
            f'Move {move_count}: Use the third move. Hydra now has {head_num} heads and {tail_num} tails.')
        # only change the move counter if this iteration didn't kill the hydra
        if head_num != 0:
            move_count += 1

    #set variable for the game to count the player's moves
    move_number = 1

    # ENTER GAME: enter a loop that allows the user to make moves until there are no more heads and tails
    while head_amt != 0 or tail_amt != 0:
        #set variable for input interpretation
        valid_move = False
        #user selects what move to use
        while not valid_move:
            move = input(f'Move {move_number}:')
            #if they enter a number, convert it to an integer to do further checks
            if move.isdigit():
                move = int(move)
                #check that it's in the proper range of available moves
                if move >= 1 and move <= 5:
                    valid_move = True
                    #if the move would force the hydra to remove more appendages than it has, make the move invalid.
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
        #check the move selected and execute it
        if move == 1:
            #move 1: remove one head and grow one back
            head_amt -= 1
            head_amt += 1
            print(f'Use the first move.', end='')
        elif move == 2:
            #move 2: remove one tail and grow two back
            tail_amt -= 1
            tail_amt += 2
            print(f'Use the second move.', end='')
        elif move == 3:
            #move 3: remove two heads
            head_amt -= 2
            print(f'Use the third move.', end='')
        elif move == 4:
            #move 4: remove two tails and grow one head
            tail_amt -= 2
            head_amt += 1
            print(f'Use the fourth move.', end='')
        elif move == 5:
            #move 5: quit the game
            print(f'\nThe Hydra slayed you.')
            break
        #if the hydra is not dead, add one to the move counter
        if head_amt != 0 or tail_amt != 0:
            move_number += 1
        print(f' The Hydra now has {head_amt} heads and {tail_amt} tails.')
        #if the hydra is dead, congratulate player
        if head_amt == 0 and tail_amt == 0:
         print(f'\nCongratulations! You killed the Hydra in {move_number} moves.')

    # report the most efficient way to kill the hydra
    print(f'The most efficient way to kill the hydra was in {move_count} moves.\n')
    # print every move to kill the hydra most efficiently
    for move in move_list:
        print(move)

    # ask the user to play again
    play_again = ''
    # enter loop to collect proper input, take only y or n
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