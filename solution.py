from game import Game
from node import Node
from copy import deepcopy


SOLVED_STATE = [2, 2, 2, 0, 1, 1, 1]

def levenshtein(board):
  """ Return levenshtein distance as heuristic"""

  distance = 0
  for b, s in zip(board, SOLVED_STATE):
    if b == s:
      distance += 1 

  return distance

def find_solution(node, use_heuristic=False):
  moves = [-2, -1, 1, 2]

  iterations = 0
  history = [node]

  seen = [node.data]
  
  while history:
    aux = history.pop(0)

    if aux.data.is_solved():
      print(f'no. iterations {iterations}')
      
      return aux.print_path()

    for move in moves:
      new_game = deepcopy(aux.data)
      new_state = new_game.move(move)

      if new_state and new_game not in seen:
        seen.append(new_game)
        node.add_child(new_game, target=aux.data)
    
    if use_heuristic:
      aux.childs.sort(key=lambda x:levenshtein(x.data.board))

    history = aux.childs + history

    iterations += 1
  
  return []