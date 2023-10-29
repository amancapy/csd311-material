"""
The loop for each game will deviate slightly from the code below depending on the needs of the game.
Teams are required to fork the repo, make the changes they think are necessary and useful, 
and make a pull request with a new file, gameloop_[game_name].py, after all teams are in agreement, 
justifying the changes in comments. You can continue PRing improvements over the duration of the course 
as long as all teams agree to each change. 

You should also add gamerules_[game_name].py with the two required functions. 
In essence, after your final changes are pulled, the whole thing should run as intended.
If you find any inconsistencies or errors with the loop logic etc., please PR changes to those as well.

!! Don't upload your actual agent code. You will submit it only during the official project submission.
For the sake of experimenting you can have your own agent be both agent_A and agent_B.
"""

import time

class Timer:
    def __init__(self):
        self.elapsed = 0
        self.running = True
        self._start = 0
    
    def resume(self):
        self.running = True
        self._start = time.perf_counter()

    def pause(self):
        self.running = False
        self.elapsed += time.perf_counter() - self._start

    def get_elapsed(self):
        return self.elapsed + (time.perf_counter() - self._start if self.running else 0)
    


from gamerules import get_future_states, check_end_conditions # gamerules.py will be the code that the teams will collaborate on, as discussed


NUM_GAMES = 100
TIME_LIMIT = 60 # seconds

a_wins, draws, b_wins = 0, 0, 0

time_A = Timer()
time_B = Timer()


for game_i in range(NUM_GAMES):
    start_state = ... # game-dependent
    (future_states, whose_turn, ...) = get_future_states(start_state, ...) # ellipsis (...) as argument to any function here implies that you have the freedom to input or output more information than specified here, excluding opponent code of course

    end = False
    while not end:
        if whose_turn == 1: # 1 == A's turn, 0 == B's turn
            from team_A import agent_A

            time_A.resume()
            choice_index = agent_A.choose_from(future_states, ...)
            chosen_state = future_states[choice_index]
            time_A.pause()
            del agent_A

            end, win_draw_loss = check_end_conditions(time_A, time_B, TIME_LIMIT, chosen_state, ...)
            if end:
                if win_draw_loss == 1:
                    a_wins += 1
                if win_draw_loss == 0:
                    draws += 1
                elif win_draw_loss == -1:
                    b_wins += 1
                break

            (future_states, _) = get_future_states(start_state, ...)


        else:
            from team_B import agent_B

            time_B.resume()
            choice_index = agent_B.choose_from(future_states, ...)
            chosen_state = future_states[choice_index]
            time_B.pause()
            del agent_B

            end, win_draw_loss = check_end_conditions(time_A, time_B, TIME_LIMIT, chosen_state, ...)
            if end:
                if win_draw_loss == 1:
                    a_wins += 1
                if win_draw_loss == 0:
                    draws += 1
                elif win_draw_loss == -1:
                    b_wins += 1
                break

            (future_states, _) = get_future_states(start_state, ...)


        print(turn_info)


print(a_wins, draws, b_wins)