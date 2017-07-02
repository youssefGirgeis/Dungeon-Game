import random
import os

CELLS = [(0,0), (1,0), (2,0), (3,0), (4,0),
		(0,1), (1,1), (2,1), (3,1), (4,1),
		(0,2), (1,2), (2,2), (3,2), (4,2),
		(0,3), (1,3), (2,3), (3,3), (4,3),
		(0,4), (1,4), (2,4), (3,4), (4,4)]

def clear_sreen():
	os.system('cls' if os.name == 'nt' else 'clear')

def get_locations():
	return random.sample(CELLS, 3)

def move_player(player, move):

	return player

def get_moves(player):
	moves = ['LEFT', 'RIGHT', 'UP', 'DOWN']

	return moves

monster, door, player = get_locations()

while True:
	print('Welcome to the Dungeon!')
	print('You are currently in room {}') # fill with player position
	print('You can move {}') # fill with availabe moves
	print('Enter QUIT to quit')

	move = input('> ')
	move = move.upper()

	if move == 'QUIT':
		break