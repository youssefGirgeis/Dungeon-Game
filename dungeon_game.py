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

def draw_map(player):
	print(' _'*5)

	tile = "|{}"

	for cell in CELLS:
		x, y = cell
		if x < 4:
			line_end = ''
			if cell == player:
				output = tile.format('X')
			else:
				output = tile.format('_')
		else:
			line_end = '\n'
			if cell == player:
				output = tile.format('X|')
			else:
				output = tile.format('_|')
		print(output, end=line_end)


def game_loop():

	monster, door, player = get_locations()
	playing = True

	while playing:
		clear_sreen()
		draw_map(player)
		valid_moves = get_moves(player)
		print('You are currently in room {}'.format(player)) # fill with player position
		print('You can move {}'.format(', '.join(valid_moves))) # fill with availabe moves
		print('Enter QUIT to quit')

		move = input('> ')
		move = move.upper()


		if move == 'QUIT':
			print('\nSee you next time!\n')
			break

		if move in valid_moves:
			player = move_player(player, move)

			if player == monster:
				print('The monster got you!!! Good luck next time!')
				playing = False

			if player == door:
				print('You escaped! Congratulations!')
				playing = False
		else:
			input('Walls are hard! Dont run into them')
	else:
		if input('Play again? [Y/n] ').lower() != 'n':
			game_loop()
		


clear_sreen()
print('Welcome to the Dungeon!')
input('Press return to start!')
clear_sreen()
game_loop()


#Make some or all of the following changes to your game:

#Change your player to a dictionary with a key that holds onto where the player has been. Then, when drawing the map, show . for every cell they've been in.
#Add more cells.
#Move the monster randomly after the player moves.
#Show the monster.
#Keep a scoreboard for multiple plays.
#Add a second or third monster.
#Add a debug mode to show where the monster(s) and door are all the time.





