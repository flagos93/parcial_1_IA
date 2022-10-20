VALID_MOVES = [-2, -1, 1, 2]


class Game:

  def __init__(self, board=[1, 1, 1, 0, 2, 2, 2]):
    self.board = board
    self.blank = self.board.index(0)

  def is_solved(self):
    """
      Return True if the game is solved, false otherwise
      * only works for 7 slots game
    """
    return self.board == [2, 2, 2, 0, 1, 1, 1]

  def swap(self, move):
    """
        Swap a piece with the blank spot
        *Internal method
    """
    b = self.blank
    m = self.blank + move

    self.board[b], self.board[m] = self.board[m], self.board[b]

    self.blank = self.board.index(0)

  def move(self, move):
    """
      Return True if the move was maketh, False otherwise
    """
    
    if move not in VALID_MOVES:
      raise Exception(f'valid moves are {VALID_MOVES}')

    piece = 2 if move > 0 else 1

    is_in_boundries = 0 <= self.blank + move < 7

    if is_in_boundries:
        is_a_piece = self.board[self.blank + move] == piece
        if is_a_piece:
          self.swap(move)
          return True
    
    return False

  def __str__(self):
    return f'>> {str(self.board)}'

  def __repr__(self):
    return f'-> {str(self.board)}'