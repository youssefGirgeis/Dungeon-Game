import random

CELLS = [(0,0), (1,0), (2,0), (3,0), (4,0),
		(0,1), (1,1), (2,1), (3,1), (4,1),
		(0,2), (1,2), (2,2), (3,2), (4,2),
		(0,3), (1,3), (2,3), (3,3), (4,3),
		(0,4), (1,4), (2,4), (3,4), (4,4)]

def get_locations():
	monster = None
	door = None
	player = None

	return (monster, door, player)

def move_player(player, move):

	return player

def get_moves(player):
	moves = ['LEFT', 'RIGHT', 'UP', 'DOWN']

	return moves

while True:
	print('Welcome to the Dungeon!')
	print('You are currently in room {}') # fill with player position
	print('You can move {}') # fill with availabe moves
	print('Enter QUIT to quit')

	move = input('> ')
	move = move.upper()

	if move == 'QUIT':
		break