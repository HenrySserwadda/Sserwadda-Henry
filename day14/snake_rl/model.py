import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F

class LinearQNet(nn.Module):

    def __init__(self,input_size,hidden_size,output_size):
        super().__init__()

        self.linear1=nn.Linear(input_size,hidden_size)
        self.linear2=nn.Linear(hidden_size,output_size)

    def forward(self,x):
        x=F.relu(self.linear1(x))
        return self.linear2(x)

class QTrainer:

    def __init__(self,model,lr,gamma):
        self.lr=lr
        self.gamma=gamma
        self.model=model
        self.optimizer=optim.Adam(model.parameters(),lr=self.lr)
        self.criterion=nn.MSELoss()