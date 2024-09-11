import time

start_time = time.time()
import tree
time_tree = time.time() - start_time

start_time = time.time()
import tree_speed
time_tree_speed = time.time() - start_time

start_time = time.time()
import labyrinth
time_labyrinth = time.time() - start_time

start_time = time.time()
import labyrinth_speed
time_labyrinth_speed = time.time() - start_time

print('-' * 100)

print(f'Tree took {time_tree} seconds')
print(f'Tree (speed) took {time_tree_speed} seconds')
print(f'The speedup is {round(time_tree / time_tree_speed * 100, 2)}%')

print(f'Labyrinth took {time_labyrinth} seconds')
print(f'Labyrinth (speed) took {time_labyrinth_speed} seconds')
print(f'The speedup is {round(time_labyrinth / time_labyrinth_speed * 100, 2)}%')