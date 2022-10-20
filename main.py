from solution import *
from copy import deepcopy


game = Game()

init_state = deepcopy(game)
game_tree = Node(init_state)

solution = find_solution(game_tree)
solution.reverse()

for state in solution:
  print(state)


print('='*24)
game_tree.fullprint()