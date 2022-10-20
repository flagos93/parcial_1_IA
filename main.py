from solution import *
from copy import deepcopy


game = Game()

# ==================
# Deep Search(ds) 
# ==================
ds_search = deepcopy(game)
ds_game_tree = Node(ds_search)

ds_solution = find_solution(ds_game_tree)
ds_solution.reverse()

print("="*24)
print("DEEP SOLUTION")
print("="*24)

for state in ds_solution:
  print(state)

print('='*24)
ds_game_tree.fullprint()

# ==================
# Better First (bf)
# ==================
bf_search = deepcopy(game)
bf_game_tree = Node(bf_search)

bf_solution = find_solution(bf_game_tree, use_heuristic=True)
bf_solution.reverse()

print("="*24)
print("BETTER FIST SOLUTION")
print("="*24)

for state in bf_solution:
  print(state)
print("="*24)

bf_game_tree.fullprint()