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

	x, y = player

	if move == 'LEFT':
		x -= 1
	if move == 'RIGHT':
		x += 1
	if move == 'UP':
		y += 1
	if move == 'DOWN':
		y += 1

	return (x, y)

def get_moves(player):
	moves = ['LEFT', 'RIGHT', 'UP', 'DOWN']
	x, y = player
	if x == 0:
		moves.remove('LEFT')
	if x == 4:
		moves.remove('RIGHT')
	if y == 0:
		moves.remove('UP')
	if y == 4:
		moves.remove('DOWN')

	return moves

monster, door, player = get_locations()

while True:
	valid_moves = get_moves(player)
	clear_sreen()
	print('Welcome to the Dungeon!')
	print('You are currently in room {}'.format(player)) # fill with player position
	print('You can move {}'.format(', '.join(valid_moves))) # fill with availabe moves
	print('Enter QUIT to quit')

	move = input('> ')
	move = move.upper()

	if move in valid_moves:
		move_player(player, move)
	else:
		print('Walls are hard! Dont run into them')
		continue

	if move == 'QUIT':
		break