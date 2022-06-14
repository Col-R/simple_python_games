# rock paper scissors
import random

def rps():
    moves = ['r', 'p', 's']
    computer_move = moves [random.randint(0,2)]
    your_move = input('Choose rock(r), paper(p), or scissors(s)').lower()

    if your_move == computer_move:
        print ("Draw, go again!")
        rps()
    else:
        if win(your_move, computer_move):
            return print (f'{your_move} beats {computer_move}. A winner is you!')
        return print (f'{computer_move} beats {your_move}. Better luck next time!')
    

def win(player, computer):
    if ((player == 'r' and computer == 's') or (player == 'p' and computer == 'r') or (player == 's' and computer == 'p')):
        return True
    else:
        return False

rps()
