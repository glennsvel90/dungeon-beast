import unittest

import dd_game



class  MoveTests(unittest.TestCase):
    def test_move_player(self):
        player = {'location': None, 'path': []}
        assert dd_game.move_player((2,2), 'LEFT') == 1,2

    def test_no_move_wall(self):
        player = {'location': None, 'path': []}
        assert dd_game.move_player((1,1), 'LEFT') == 1,1
