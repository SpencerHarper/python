#!/usr/bin/env python
# ocw10-rock_paper_scissors.py

def rps(x, y):
	winner = 'none'
	if x == 'rock' and y == 'rock':
		winner = 'tie'
	elif x == 'paper' and y == 'rock':
		winner = 'player 2'
	elif x == 'scissors' and y == 'rock':
		winner = 'player 2'
	elif x == 'rock' and y == 'paper':
		winner = 'player 2'
	elif x == 'paper' and y == 'paper':
                winner = 'tie'
	elif x == 'scissors' and y == 'paper':
                winner = 'player 1'
	elif x == 'rock' and y == 'scissors':
                winner = 'player 2'
	elif x == 'paper' and y == 'scissors':
                winner = 'player 2'
	elif x == 'scissors' and x == 'scissors':	
		winner = 'tie'
	else:
		winner = 'This is not a valid object selection.'
	
	print winner

player1 = raw_input('enter rock, paper, or scissors: ')
player2 = raw_input('enter rock, paper, or scissors: ')

rps(player1, player2)

