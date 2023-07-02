# tic_tac_toe/logic/exceptions.py

class InvalidGameState(Exception):
    '''Raise when the game state is invalid.'''

class InvalidMove(Exception):
    '''Raise when the move is invalid'''
    
class UnknownGameScore(Exception):
    '''Raise when the game score is unknown'''