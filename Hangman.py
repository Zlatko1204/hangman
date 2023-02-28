#! python3

def hangman(word):
    word = word
    letters = []
    wrong_guesses = 0
    stages = ["","_____  ","|  |  ","|  O  ","| /|\\  ","| / \\  ","|    "]
    letters_left = list(word)
    score_board = ['_']* len(word)
    win = False
    print('Welcome to Hang Man')
    print()
    print(''.join(score_board))

    while wrong_guesses < len(stages)-1:
        print('\n')
        print('Letters used : {}' .format(letters))
        guess = input('Guess a letter : ')
        letters.append(guess)
        if guess in letters_left:
            while guess in letters_left:
                character_index = letters_left.index(guess)
                score_board[character_index]=guess
                letters_left[character_index]='$'   
        else:
            wrong_guesses += 1
        print(''.join(score_board))
        print('\n'.join(stages[0 : wrong_guesses + 1]))
        if '_' not in score_board:
            print('You win! The word was:')
            print(''.join(score_board))
            win = True
            break
    if not win:
        print('\n'.join(stages[0:wrong_guesses+1]))
        print('You lose! The word was {}' .format(word))
hangman('hangman')