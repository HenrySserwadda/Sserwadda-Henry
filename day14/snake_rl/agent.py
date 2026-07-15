import random
import numpy as np
import torch
from collections import deque

MAX_MEMORY=100000
BATCH_SIZE=1000
LR=0.001

class Agent:

    def __init__(self):
        self.n_games=0
        self.epsilon=0
        self.gamma=0.9
        self.memory=deque(maxlen=MAX_MEMORY)

    def remember(self,state,action,reward,next_state,done):
        self.memory.append((state,action,reward,next_state,done))

    def get_action(self,state):

        self.epsilon=80-self.n_games

        final_move=[0,0,0]

        if random.randint(0,200)<self.epsilon:
            move=random.randint(0,2)
        else:
            move=0

        final_move[move]=1

        return final_move