from game import SnakeGame
from agent import Agent

def train():

    game=SnakeGame()
    agent=Agent()

    while True:

        state_old=[]

        action=agent.get_action(state_old)

        reward,done,score=game.play_step(action)

        state_new=[]

        agent.remember(state_old,action,reward,state_new,done)

        if done:
            game.reset()
            agent.n_games+=1
            print("Game",agent.n_games,"Score",score)

if __name__=="__main__":
    train()