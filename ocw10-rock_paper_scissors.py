#!/usr/bin/env python
# ocw10-rock_paper_scissors.py

def valid(input):
	if input == 'paper' or input == 'rock' or input == 'scissors':
		return True
	else:
		return False

def rps2(player1, player2):
	if valid(player1) and valid(player2):
		if player1 == player2:
			return 'Tie!'
		elif player1 == 'rock' and player2 == 'scissors' or\
		player1 == 'paper' and player2 == 'rock' or\
		player1 == 'scissors' and player2 == 'paper':
			return 'Player 1 Wins!!!'
		else:
			return 'Player 2 Wins!!!'
	else:
		return "Invalid input - please enter 'rock', 'paper', or 'scissors'"

def rps(x, y):
	winner = 'none'
	if x == y:
		winner = 'tie'
	elif x == 'paper' and y == 'rock':
		winner = 'player 2'
	elif x == 'scissors' and y == 'rock':
		winner = 'player 2'
	elif x == 'paper' and y == 'scissors':
		winner = 'player 2'
	elif x == 'rock' and y == 'paper':
		winner = 'player 1'
	elif x == 'scissors' and y == 'paper':
                winner = 'player 1'
	elif x == 'rock' and y == 'scissors':
                winner = 'player 1'
	else:
		winner = 'This is not a valid object selection.'

	print winner

input = raw_input('game version \'1\' or \'2\'?: ')

if input == 1:
	player1 = raw_input('enter rock, paper, or scissors: ')
	player2 = raw_input('enter rock, paper, or scissors: ')
	rps(player1, player2)
else:
	player1 = raw_input('enter rock, paper, or scissors: ')
	player2 = raw_input('enter rock, paper, or scissors: ')
	print rps2(player1, player2)



