from solution import *
from copy import deepcopy


game = Game()

# ==================
# Deep Search(ds) 
# ==================
ds_search = deepcopy(game)
ds_game_tree = Node(ds_search)

print("="*24)
print("DEEP SOLUTION")
ds_solution = find_solution(ds_game_tree)
print("="*24)

ds_solution.reverse()

for state in ds_solution:
  print(state)

print('='*24)
ds_game_tree.fullprint()

# ==================
# Better First (bf)
# ==================
bf_search = deepcopy(game)
bf_game_tree = Node(bf_search)

print("="*24)
print("BETTER FIST SOLUTION")
bf_solution = find_solution(bf_game_tree, use_heuristic=True)
print("="*24)

bf_solution.reverse()

for state in bf_solution:
  print(state)
print("="*24)

bf_game_tree.fullprint()