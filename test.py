from torch.nn import ReLU
import numpy as np
import torch.nn as nn

class Test(nn.Module):
    def __init__(self) -> None:
        super(Test, self).__init__()
        self.conv1 = nn.Conv2d(3, 64, 5)
        self.pool = nn.MaxPool2d(2,2)

    def forward(self, x):
        x = self.conv1(F )

