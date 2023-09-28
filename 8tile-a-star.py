import random

# when the 3x3 grid is laid out flat, what is the change of index when an action U/D/L/R is performed, if valid?
action_index_change = {"U": -3, "D": +3, "L": -1, "R": +1}
oppossite_actions = {"U": "D", "D": "U", "L": "R", "R": "L", "S": None}
start_state = [1, 2, 3, 4, 5, 6, 7, 8, 0] # before shuffling
    
h1 = lambda x: len([i == j for i, j in zip(x[0], [1, 2, 3, 4, 5, 6, 7, 8, 0]) if i == j]) # num_tiles out of place
h2 = lambda x: -sum([abs(((x[0][i] - 1) % 9 - ((x[0][i] - 1) % 9) % 3) / 3 - (i - i % 3) / 3) + abs(((x[0][i] - 1) % 9) % 3 - i % 3) for i in range(9)]) / 2 # manhattan
pick = h1

# a_star = heuristic * inadmissibility_factor + route_length
key = lambda x: pick(x) * 100 - len(x[1])

for i in range(1000):
    # inversion parity test for whether random state is solvable.
    inversions = 1
    while inversions % 2 != 0:
        random.shuffle(start_state)
        inversions = sum([len([start_state[j] > start_state[i] for i in range(len(start_state)) for j in range(i, len(start_state)) if start_state[j] > start_state[i] and start_state[i] != 0])])

    print(i, start_state, end=" ")

    queue = [(start_state, "S", 0)] # "S" => starting
    visited = {} # remember hashing?

    while queue: # while queue is not empty
        queue.sort(key=lambda x: x[2])
        # print(len(visited), a_star(queue[-1]))

        curr_state = queue.pop()
        visited[tuple(curr_state[0])] = curr_state[1] # lists are not hashable, but tuples are.

        curr_zero_idx = curr_state[0].index(0) # find index of 0
        for drn in set(("U", "D", "L", "R")).difference([oppossite_actions[curr_state[1][-1]]]):
            if (curr_zero_idx % 3 == 0 and drn == "L") or ((curr_zero_idx + 1) % 3 == 0 and drn == "R"): # can't left or right when at border. the U/D doesn't need to be edge-cased
                continue
            new_zero_idx = curr_zero_idx + action_index_change[drn]

            if 0 <= new_zero_idx < 9: # this is where U/D at border solves itself
                temp_state = [i for i in curr_state[0]] # this makes a deep copy
                temp_state[curr_zero_idx], temp_state[new_zero_idx] = temp_state[new_zero_idx], temp_state[curr_zero_idx] # a, b = b, a => switch the values of a and b
                
                if tuple(temp_state) not in visited or (tuple(temp_state) in visited and len(visited[tuple(temp_state)]) > len(curr_state[1]) + 1):
                    subtuple = (temp_state, curr_state[1] + drn)
                    queue.append((*subtuple, key(subtuple)))
                
                if temp_state == [1, 2, 3, 4, 5, 6, 7, 8, 0]:
                    print(curr_state[1] + drn[1:], len(curr_state[1]), len(visited))
                    queue = []
                    break
