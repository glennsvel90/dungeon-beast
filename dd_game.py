"""Dungeon Game
Escape from the dungeon. Try to find the hidden door and escape. But be careful! There is beast hiding somewhere inside!
"""

import os
import random

GAME_DIMENSIONS = (5, 5)
player = {'location': None, 'path': []}


def clear():
    """ clear the terminal """
    
    os.system('cls' if os.name == 'nt' else 'clear')


def build_cells(width, height):
    """ Create and return a 'width' x 'height' grid of two-tuples, making the cells for the map.
    
    >>> cells = build_cells(2, 2)
    >>> len(cells)
    4
    
    """
    cells = []
    for y in range(height):
        for x in range(width):
            cells.append((x, y))
    return cells


def get_locations(cells):
    """ Make the player, door, and monster appear in different random locations
    
    >>> cells = build_cells(3, 3)
    >>> m, d, p = get_locations(cells)
    >>> m != d and d != p
    True
    >>> d in cells
    True
    
    """
    monster = random.choice(cells)
    door = random.choice(cells)
    player = random.choice(cells)

    if monster == door or monster == player or door == player:
        monster, door, player = get_locations(cells)

    return monster, door, player


def get_moves(player):
    ''' Show and return the available moves for the player '''
    
    x, y = player
    moves = ['LEFT', 'RIGHT', 'UP', 'DOWN']
    if x == 0:
        moves.remove('LEFT')
    if x == GAME_DIMENSIONS[0] - 1:
        moves.remove('RIGHT')
    if y == 0:
        moves.remove('UP')
    if y == GAME_DIMENSIONS[1] - 1:
        moves.remove('DOWN')
    return moves


def move_player(player, move):
    ''' moves the player to available directions '''
    
    x, y = player['location']
    player['path'].append((x, y))
    if move == 'LEFT':
        x -= 1
    elif move == 'UP':
        y -= 1
    elif move == 'RIGHT':
        x += 1
    elif move == 'DOWN':
        y += 1
    return x, y


def draw_map(cells):
    ''' Shows the player and his/her footsteps in the map '''
    
    print(' _'*GAME_DIMENSIONS[0])
    row_end = GAME_DIMENSIONS[0]
    tile = '|{}'
    for index, cell in enumerate(cells):
        if index % row_end < row_end - 1:
            if cell == player['location']:
                print(tile.format('X'), end='')
            elif cell in player['path']:
                print(tile.format('.'), end='')
            else:
                print(tile.format('_'), end='')
        else:
            if cell == player['location']:
                print(tile.format('X|'))
            elif cell in player['path']:
                print(tile.format('.|'))
            else:
                print(tile.format('_|'))

def play():
    ''' runs the game loop '''
    cells = build_cells(*GAME_DIMENSIONS)
    monster, door, player['location'] = get_locations(cells)

    while True:
        clear()

        print("WELCOME TO THE DUNGEON!")
        moves = get_moves(player['location'])

        draw_map(cells)

        print("\nYou're currently in room {}".format(player['location']))
        print("\nYou can move {}".format(', '.join(moves)))
        print("Enter QUIT to quit")

        move = input("> ")
        move = move.upper()

        if move in ['QUIT', 'Q']:
            break

        if move not in moves:
            print("\n** Walls are hard! Stop running into them! **\n")
            continue

        player['location'] = move_player(player, move)

        if player['location'] == door:
            print("\n** You escaped! **\n")
            break
        elif player['location'] == monster:
            print("\n** You got eaten! **\n")
            break

if __name__ == '__main__':
    play()
