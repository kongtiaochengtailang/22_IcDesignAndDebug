import torch
from torch import nn

class MyLeNet5(nn.Module):
    def __init__(self):
        super(MyLeNet5, self).__init__()

        # self.conv1 = nn.Conv2d(in_channels=1, out_channels=16, kernel_size=5, padding=1)
        # self.Sigmoid = nn.Sigmoid()
        # self.pool1 = nn.AvgPool2d(kernel_size=2, stride=2)
        # self.conv2 = nn.Conv2d(in_channels=16, out_channels=32, kernel_size=5, padding=1)
        # self.pool2 = nn.AvgPool2d(kernel_size=2, stride=2)

        self.conv1 = nn.Conv2d(in_channels=1, out_channels=6, kernel_size=5, padding=2)
        self.Sigmoid = nn.Sigmoid()
        self.pool1 = nn.AvgPool2d(kernel_size=2, stride=2)
        self.conv2 = nn.Conv2d(in_channels=6, out_channels=16, kernel_size=5)
        self.pool2 = nn.AvgPool2d(kernel_size=2, stride=2)
        self.conv3 = nn.Conv2d(in_channels=16, out_channels=120, kernel_size=5)

        self.flatten = nn.Flatten()
        # self.dense = nn.Linear(32, 128)
        # n = 10
        # self.output = nn.Linear(128, n)
        self.dense = nn.Linear(120, 84)
        n = 65
        self.output = nn.Linear(84, n)

    def forward(self, x):
        x = self.Sigmoid(self.conv1(x))
        x = self.pool1(x)
        x = self.Sigmoid(self.conv2(x))
        x = self.pool2(x)
        x = self.conv3(x)
        x = self.flatten(x)
        x = self.dense(x)
        x = self.output(x)

        return x

if __name__=="__main__":
    x = torch.rand(1, 1, 28, 28)
    model = MyLeNet5()
    y = model(x)
